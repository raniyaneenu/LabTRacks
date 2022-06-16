from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import mainFunctions
from . models import *
from CustomerBilling.models import *
from django.contrib import messages
from . forms import *

# Create your views here.

searchbill=CustomerBilling.objects.all()


def topmenu(request):   
    return render(request,'nav.html',{'billsearch':searchbill})

def homepg(request): 
    return render(request,'home.html',{'billsearch':searchbill})

@login_required(login_url='Login')
def addTest(request):
    tst=Test.objects.all()
    cat=TestCategory.objects.all()
    if request.method=='POST':
        ct=request.POST['categ']
        try:
            ct1=TestCategory.objects.get(id=ct)
            tst=request.POST['testnm']
            pr=request.POST['testpr']
            sp=request.POST['spec']
            nr=request.POST['nor']
            dr=request.POST['dur']

            if(ct=='' or tst=='' or pr=='' or sp=='' or nr=='' or dr==''):
                messages.info(request,'please fill all the fields!!!')
            else:
                t=Test()
                t.Test_name=tst
                t.Test_price=pr
                t.speciment_det=sp
                t.normal_range=nr
                t.duration=dr
                t.categ=ct1
                t.save()
                return redirect('home')

        except:
            messages.info(request,'Category not found. Try existing category')
    return render(request,'AddTest.html',{'test':tst,'categ':cat,'billsearch':searchbill})

@login_required(login_url='Login')
def addCategory(request):
    cat=TestCategory.objects.all()
    if request.method=='POST':
        ct=request.POST['categ']
        if(ct==''):
            messages.info(request,'please fill all the fields!!!')
        else:
            catg=TestCategory()
            catg.name=ct
            catg.save()

            return redirect('home')

    return render(request,'AddCateg.html',{'categ':cat,'billsearch':searchbill})

@login_required(login_url='Login')
def addHospitalFun(request):
    hsp=Hospital.objects.all()
    if request.method=='POST':
        name=request.POST['hospnm']
        adr=request.POST['hospadd']
        if(name=='' or adr==''):
            messages.info(request,'please fill all the fields!!!')
        else:
            mainFunctions.HospitalAdding(name,adr)
            return redirect('HospitalList')

    return render(request,'AddHospital.html',{'hs':hsp,'billsearch':searchbill})

@login_required(login_url='Login')
def addDoctorHos(request):
    hsp=Hospital.objects.all()
    doc=Doctors.objects.all()
    if request.method=='POST':
        dname=request.POST['docnm']
        hname=request.POST['hospnm']
        if(dname=='' or hname==''):
            messages.info(request,'please fill all the fields!!!')
        else:
            dnm=Doctors.objects.get(id=dname)
            hnm=Hospital.objects.get(id=hname)
            mainFunctions.DocHosAdding(dnm,hnm)
            return redirect('DoctorsList')
    return render(request,'AddDoctorHos.html',{'hs':hsp,'dc':doc,'billsearch':searchbill})

@login_required(login_url='Login')
def DocView(request):
    doc=Doctors.objects.all()
    hs=Doctor_Hospital.objects.all()

    return render(request,'ViewDoctors.html',{'dc':doc,'h':hs,'billsearch':searchbill})

@login_required(login_url='Login')
def AddDoctor(request):

    doc=Doctors.objects.all()
    
    if request.method=='POST':
        dname=request.POST['docnm']
        dep=request.POST['deptnm']
        if(dname=='' or dep==''):
            messages.info(request,'please fill all the fields!!!')
        else:
            mainFunctions.DoctorAdding(dname,dep)
            return redirect('DoctorsList')

    return render(request,'AddDoctor.html',{'dc':doc,'billsearch':searchbill})

@login_required(login_url='Login')
def HospitalList(request):
    hos=Hospital.objects.all()
    return render(request,'ViewHospital.html',{'hos':hos,'billsearch':searchbill})

@login_required(login_url='Login')
def CategList(request):
    catg=TestCategory.objects.all()
    return render(request,'ViewCateg.html',{'cat':catg,'billsearch':searchbill})

@login_required(login_url='Login')
def TestList(request):
    test=Test.objects.all()
    return render(request,'ViewTest.html',{'tst':test,'billsearch':searchbill})


@login_required(login_url='Login')
def EditTest(request,tid):
    testedt=get_object_or_404(Test,id=tid)
    cat=TestCategory.objects.all()
    edt=TestForm(request.POST or None, instance=testedt)
    if edt.is_valid():
        edt.save()
        return redirect('TestList')
    return render(request,'EditTest.html',{'tst':edt,'ct':cat})

@login_required(login_url='Login')
def EditCategory(request,cid):
    catEdit=get_object_or_404(TestCategory,id=cid)
    edt=CategoryForm(request.POST or None, instance=catEdit)
    if edt.is_valid():
        edt.save()
        return redirect('CategoryList')
    return render(request,'EditCategory.html',{'edt':edt})

@login_required(login_url='Login')
def EditDoctor(request,did):
    docEdit=get_object_or_404(Doctors,id=did)
    edt=DoctorsForm(request.POST or None, instance=docEdit)
    if edt.is_valid():
        edt.save()
        return redirect('DoctorsList')
    return render(request,'EditDoctor.html',{'edt':edt})

@login_required(login_url='Login')
def EditHospital(request,hid):
    hosEdit=get_object_or_404(Hospital,id=hid)
    edt=HospitalForm(request.POST or None, instance=hosEdit)
    if edt.is_valid():
        edt.save()
        return redirect('HospitalList')
    return render(request,'EditHospital.html',{'edt':edt})




    
