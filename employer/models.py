from django.db import models
from django import forms
from django.db import models
from django.contrib.auth.models import User

class titleChoices(models.TextChoices):
    MRS = 'Mrs'
    MR = 'Mr'
    MS = 'Ms'
    DR = 'Dr'
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employer')
    image = models.ImageField(upload_to='images/', blank=False, null=True)
    title = models.CharField(max_length=3, choices=[(tag, tag.value) for tag in titleChoices], default=titleChoices.MR)
    firstname = models.CharField(max_length=20 )
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15 )
    address = models.TextField(blank=True, null=True, max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
class Job(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True)
    company_logo = models.ImageField(upload_to='job_logos/', blank=True)
    is_published = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

