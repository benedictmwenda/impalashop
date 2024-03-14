from django.db import models

# Create your models here.


class Client(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    email=models.EmailField()


    def __str__(self):
        return self.name
