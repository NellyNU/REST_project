from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(default='default@example.com')
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name

