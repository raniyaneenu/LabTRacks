
from . models import *

def addingCustomer(name,phone,mail,addr,age,gender,usr):
    cus=Customer()
    cus.name=name
    cus.phone=phone
    cus.email=mail
    cus.address=addr
    cus.age=age
    cus.gender=gender
    cus.updated_by=usr
    cus.save()