from django.urls import path
from .views import*
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('new/', EntryCreateView.as_view(), name='entry_create'),
    path('<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register_view , name='register'),
    path('about/', about, name='about'),
    path('help/', help_and_suggestions, name='help'),

]
