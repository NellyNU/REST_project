from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


# Create your models here.
class Contacts(models.Model):


    STATUS_CHOICES = [
        ('under_review', 'Under Review'),
        ('appeal', 'Appeal'),
        ('cassation', 'Cassation'),
        ('preparation', 'Preparation'),
        ('completed', 'Completed')
    ]
    
    data = models.DateTimeField(default=datetime.now)  
    plaintiff = models.CharField(max_length=255, default='Unknown Plaintiff')
    defendant = models.CharField(max_length=255,  default='Unknown Defendant')
    executionOrder = models.BooleanField(default=False)
    
    under_review = models.BooleanField(default=False)
    appeal = models.BooleanField(default=False)
    cassation = models.BooleanField(default=False)
    preparation = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    
    notes = models.TextField()

    def __str__(self):
        return f"Case {self.id}: {self.plaintiff} vs {self.defendant}"
    
class Status(models.Model):
    under_review = models.BooleanField(default=False)
    appeal = models.BooleanField(default=False)
    cassation = models.BooleanField(default=False)
    preparation = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Status: {'Under Review' if self.under_review else ''} {'Appeal' if self.appeal else ''} {'Cassation' if self.cassation else ''} {'Preparation' if self.preparation else ''} {'Completed' if self.completed else ''}"
