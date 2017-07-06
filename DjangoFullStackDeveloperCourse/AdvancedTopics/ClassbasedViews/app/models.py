from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=264)
    principal = models.CharField(max_length=255)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('app:Detail',kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='studentOf')

    def __str__(self):
        return self.name
