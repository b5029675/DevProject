from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Request(models.Model):
    type = models.CharField(max_length = 100 , choices = [('Friends', 'Friends'), ('Players', 'Players')])
    game = models.CharField(max_length = 100 , choices = [('N/A', 'N/A'), ('Dota2', 'Dota2'), ('Counter-Strike 2', 'Counter-Strike 2'), ('Valorant', 'Valorant')])
    details = models.TextField()
    date_submitted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, related_name = 'requests',
    on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.author} is looking for {self.type}'
    def get_absolute_url(self):
        return reverse('itreporting:request-detail', kwargs = {'pk': self.pk})