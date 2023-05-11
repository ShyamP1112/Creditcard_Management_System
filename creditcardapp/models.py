from django.db import models
from datetime import datetime

# Create your models here.
class usersignup(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=20)

class creditcardapply(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    mothername=models.CharField(max_length=150)
    jobdesignation=models.CharField(max_length=150)
    sallary=models.BigIntegerField()
    birthdate=models.DateField()
    address=models.TextField()
    city=models.CharField(max_length=100)
    pincode=models.BigIntegerField()
    aadharcard=models.FileField(upload_to='AadharCard')
    pancard=models.FileField(upload_to='PanCard')
    userimages=models.FileField(upload_to='UserImages')
    bankstatement=models.FileField(upload_to='BankStatement')
    sllaryslip=models.FileField(upload_to='Sallaryslip')
    selectbank=models.CharField(max_length=150)
    gender=models.CharField(max_length=100)
   

class contacts(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=50)
    phonenumber=models.BigIntegerField()
    email=models.EmailField()
    massage=models.TextField()
   