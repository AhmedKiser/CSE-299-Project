from django.db import models


# Create your models here.
class user(models.Model):
    # uID = models.IntegerField(null=True)
    uName = models.CharField(max_length=40)
    uMail = models.EmailField(max_length=30)
    uPhone = models.CharField(max_length=15)
    uDOB = models.DateField()
    uPassword = models.CharField(max_length=40)
    # repassword = models.CharField(max_length=40)

