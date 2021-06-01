from django.db import models


class User(models.Model):
    fristname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    emails = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username


class Accounts(models.Model):
    username = models.CharField(max_length=50)
    accountnum = models.CharField(max_length=150, unique=True)
    acctype = models.CharField(max_length=40)
    min_bal = models.FloatField(max_length=150)

    def __str__(self):
        return self.min_bal
