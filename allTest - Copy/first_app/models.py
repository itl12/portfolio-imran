from django.db import models

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to='profile_pic')
    date = models.DateField(auto_now_add=True)

    