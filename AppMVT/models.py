from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    family_relationship = models.CharField(max_length=30)
