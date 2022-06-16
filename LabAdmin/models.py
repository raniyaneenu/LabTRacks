from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserRoles(models.Model):
    name=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class user_logins(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    address=models.TextField()
    dob=models.DateTimeField()
    role=models.ForeignKey(UserRoles,on_delete=models.CASCADE,null=True,blank=True)
    gender=models.CharField(max_length=10)
    user_status=models.CharField(max_length=15,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)



class TestCategory(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Test(models.Model):
    Test_name=models.CharField(max_length=100)
    Test_price=models.FloatField()
    speciment_det=models.CharField(max_length=100,null=True,blank=True)
    normal_range=models.CharField(max_length=250,null=True,blank=True)
    duration=models.CharField(max_length=55,null=True,blank=True)
    categ=models.ForeignKey(TestCategory,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.id)
   


class Hospital(models.Model):
    Hospital_Name=models.CharField(max_length=50)
    Hospital_Address=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    

class Doctors(models.Model):
    Doc_Name=models.CharField(max_length=25)
    Doc_Department=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class Doctor_Hospital(models.Model):
    Doctor_Name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Hospital_Name=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
  