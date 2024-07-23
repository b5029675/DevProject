from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Request(models.Model):
    type = models.CharField(max_length = 100 , choices = [('Friends', 'Friends'), ('Players', 'Players')])
    game = models.CharField(max_length = 100)
    details = models.TextField()
    date_submitted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, related_name = 'requests',
    on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.author} is looking for {self.type}'