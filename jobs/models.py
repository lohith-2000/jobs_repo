from django.db import models
#Create your models here.
from django.contrib.auth.models import User
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interviewed', 'Interviewed'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    applied_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.company + " - " + self.role
