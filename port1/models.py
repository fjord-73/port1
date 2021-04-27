from django.db import models
import os
# Create your models here.

class Datasample(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    birthday = models.DateField()

    def __str__(self):
        return 'Datasample:id'+str(self.name)

class UploadFile(models.Model):
    file = models.FileField(upload_to='media/')
    def urls(self):
        return self.file.url
    def name(self):
        return self.file.name