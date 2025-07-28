from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Entry
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def form_valid(self, form):
    messages.success(self.request, "Entrée créée avec succès !" if not self.object else "Entrée modifiée avec succès !")
    return super().form_valid(form)


class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'journal/entry_list.html'

    def get_queryset(self):
        return Entry.objects.filter(author=self.request.user).order_by('-created_at')
    
class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'content', 'photos']
    template_name = 'journal/entry_create.html'
    success_url = reverse_lazy('entry_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    fields = ['title', 'content', 'photos']
    template_name = 'journal/entry_create.html'
    success_url = reverse_lazy('entry_list')

    def test_func(self):
        entry = self.get_object()
        return self.request.user == entry.author


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    template_name = 'journal/entry_delete.html'
    success_url = reverse_lazy('entry_list')

    def test_func(self):
        entry = self.get_object()
        return self.request.user == entry.author
    

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès ! Connecte-toi maintenant.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
def about(request):
    return render(request, 'about.html')

def help_and_suggestions(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Envoi du mail
        send_mail(
            f'Nouvelle suggestion de {name}',
            message,
            email,
            ['support@journal.com'],
            fail_silently=False,
        )
        
        return HttpResponse("Merci pour votre suggestion, nous vous répondrons bientôt.")
    
    return render(request, 'FAQ.html')

