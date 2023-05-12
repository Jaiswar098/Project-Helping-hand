from django.db import models

# Create your models here.
class UserTypeChoice(models.TextChoices):
    JOBSEEKER = 'JS', 'Job Seeker'
    RECRUITER = 'RC', 'Recruiter'
class Profile(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user_type = models.CharField(max_length=2, choices=UserTypeChoice.choices, default=UserTypeChoice.JOBSEEKER)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username