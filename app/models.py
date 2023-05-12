from django.db import models

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name