from django.db import models

# Create your models here.
class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'book'