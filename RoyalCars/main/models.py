from django.db import models
from django.conf import settings

from RoyalCars.settings import BASE_DIR

def handle_uploaded_file(f):
    url = str(BASE_DIR) + '\media\pictures'
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="pictures")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class Form(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"

    def __str__(self):
        return self.full_name