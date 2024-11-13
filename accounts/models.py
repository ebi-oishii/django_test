from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    profile_image = models.ImageField(verbose_name="プロフィール画像", null=True, black=True)
    
