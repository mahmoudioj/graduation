from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="media")

    def __str__(self):
        return self.name
