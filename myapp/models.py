from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
