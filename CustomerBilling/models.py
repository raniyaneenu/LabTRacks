from django.db import models
from django.contrib.auth.models import User
from LabAdmin.models import *
import jsonfield

# Create your models here.
class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T','Trans')
    )
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=25)
    email=models.CharField(max_length=255)
    address=models.TextField()
    age=models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    updated_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class CustomerBilling(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    customer_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=5)
    is_child=models.CharField(max_length=5,null=True,blank=True)
    phone=models.CharField(max_length=25)
    email=models.CharField(max_length=255)
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE,null=True,blank=True)
    doc_name=models.CharField(max_length=100,null=True,blank=True)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True,blank=True)
    hosp_name=models.CharField(max_length=100,null=True,blank=True)
    amount=models.FloatField()
    discount_total=models.FloatField(null=True,blank=True)
    total_amount=models.FloatField(null=True,blank=True)
    count=models.IntegerField(null=True,blank=True)
    archived=models.CharField(max_length=5,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    updated_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class BillingTestData(models.Model):
    billid=models.ForeignKey(CustomerBilling,on_delete=models.CASCADE)
    test=jsonfield.JSONField(null=True,blank=True)
    discount=jsonfield.JSONField(null=True,blank=True)

    def __str__(self):
        return str(self.id)


class fin_transactions(models.Model):
    billid=models.ForeignKey(CustomerBilling,on_delete=models.CASCADE)
    payment_mode=models.CharField(max_length=25,null=True,blank=True)
    comments=models.CharField(max_length=350,null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    updated_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.billid)
    

class originalBillTemplates(models.Model):
    billsample=models.FileField(upload_to='billing')

class originalResultTemplates(models.Model):
    testsample=models.FileField(upload_to='testresult')
    
class UserBill(models.Model):
    billid=models.ForeignKey(CustomerBilling,on_delete=models.CASCADE)
    billdetails=models.FileField(upload_to='customerBill')
    resultdetails=models.FileField(upload_to='customerResult',null=True,blank=True)