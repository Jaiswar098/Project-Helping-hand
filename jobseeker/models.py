from django.db import models
from employer.models import Job
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=False, null=True)
    name = models.CharField(max_length=50 )
    email = models.EmailField()
    phone = models.CharField(max_length=15 )
    address = models.TextField(blank=True, null=True, max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    education = models.CharField("Highest Education ", max_length=15 ,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.job.title 