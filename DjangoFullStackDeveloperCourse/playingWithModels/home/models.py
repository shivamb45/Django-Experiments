from django.db import models

# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True,help_text="Email-ID is unique per person.")

    def __str__(self):
        return self.email
