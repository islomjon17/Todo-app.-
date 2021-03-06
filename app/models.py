from django.db import models
#import user model from django.contrib.auth.models
from django.contrib.auth.models import User

### To do models
class TODO(models.Model):
    status_choices = [
    ('DONE', 'TUGATILDI'),
    ('DOING', 'BAJARILMOQDA'),
    ]
    nom = models.CharField(max_length=50)
    jarayon = models.CharField(max_length=15 , choices=status_choices)
    sana = models.DateTimeField(auto_now_add=True)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)