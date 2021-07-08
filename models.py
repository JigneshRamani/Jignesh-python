from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    avtar = models.CharField(max_length=150)

    class Meta:
        db_table = 'Users'