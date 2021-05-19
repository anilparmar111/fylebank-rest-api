from django.db import models

# Create your models here.


class Bank(models.Model):
    id = models.BigIntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=49)

    def __str__(self):
        return self.name


class Branche(models.Model):
    bank_id = models.BigIntegerField()
    ifsc = models.CharField(max_length=11, null=False)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    def __str__(self):
        return self.branch
