from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    photos = models.ImageField(upload_to='photos/', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entrée'
        verbose_name_plural = 'Entrées'

    @property
    def excerpt(self):
        return self.content[:100] + '...' if len(self.content) > 100 else self.content
