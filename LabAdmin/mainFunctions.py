from . models import *

def HospitalAdding(name,addr):

    hos=Hospital()
    hos.Hospital_Name=name
    hos.Hospital_Address=addr
    hos.save()
    print('added')

def DoctorAdding(dname,dep):
    doc=Doctors()
    doc.Doc_Name=dname
    doc.Doc_Department=dep
    doc.save()

def DocHosAdding(dname,hname):
    dh=Doctor_Hospital()
    dh.Doctor_Name=dname
    dh.Hospital_Name=hname
    dh.save()
    