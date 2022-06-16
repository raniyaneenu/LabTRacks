from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import functions
from LabAdmin.models import *
from . models import *
import datetime
from datetime import date
from docx import Document
from django.core.files.storage import default_storage
from django.http import HttpResponse
from . billing import *
from django.contrib import messages

# Create your views here.
searchbill=CustomerBilling.objects.all()

@login_required(login_url='Login')
def searching(request):
    bid=request.GET['srid']
    try:
        cust=CustomerBilling.objects.get(id=bid)
        bills=BillingTestData.objects.get(billid=cust.id)
        test=Test.objects.all()
        return render(request,'billResult.html',{'test':test,'cus':cust,'bill':bills,'billsearch':searchbill})
    except:
        messages.info(request,'No query matches this search. please try another')
    return render(request,'billResult.html',{'billsearch':searchbill})

@login_required(login_url='Login')
def LabTracksBilling(request):
    cst=Customer.objects.all()
    tst=Test.objects.all()
    doctds=Doctors.objects.all()
    hospds=Hospital.objects.all()
    

    if request.method=='POST':
        tot=0
        testdata={}
        disdict={}
        usr=request.POST['customer']
        tsnm=request.POST.getlist('name')
        testid=request.POST.getlist('id')
        pr=request.POST.getlist('price')
        doc=request.POST['doctor']
        hos=request.POST['hospital']
        disc=request.POST.getlist('discount')
        child=request.POST.get('child')

        if(usr==''):
            messages.info(request,'please fill Name field!!!')
        if(doc==''):
            messages.info(request,'please fill Doctor Name field!!!')
        if(hos==''):
            messages.info(request,'please fill Hospital Name field!!!')
        elif(tsnm==[] or testid==[] or pr==[]):
            messages.info(request,'please add at least one test to continue!!!!')

        else:
            try:
                docdata=Doctors.objects.get(id=doc)
                hosdata=Hospital.objects.get(id=hos)
        
                dis=0
                for i in pr:
                    tot+=float(i)
                    
                
                for j in range(0,len(testid)):
                    prd=Test.objects.get(id=testid[j])
                    testdata['test'+str(j+1)]=str(prd)
                    dis+=float(disc[j])
                    disdict[str(prd)]=str(disc[j])
                print(disdict)
                final=tot-dis        
                try:

                    cus=Customer.objects.get(id=usr)
                    print('customer: ',cus)
                    cusBill=CustomerBilling()
                    cusBill.customer_id=cus
                    cusBill.customer_name=cus.name
                    cusBill.gender=cus.gender

                    if(child=='option1'):
                        cusBill.is_child='Yes'
                    else:
                        cusBill.is_child='No'
                
                    cusBill.phone=cus.phone
                    cusBill.email=cus.email
                    cusBill.doctor=docdata
                    cusBill.doc_name=docdata.Doc_Name
                    cusBill.hospital=hosdata
                    cusBill.hosp_name=hosdata.Hospital_Name
                    cusBill.amount=tot
                    cusBill.discount_total=dis
                    cusBill.total_amount=final
                    cusBill.updated_by=request.user
                    cusBill.save()

                    billdata=BillingTestData()
                    billdata.billid=cusBill
                    billdata.test=testdata
                    billdata.discount=disdict
                    billdata.save()

                    trans=fin_transactions()
                    trans.billid=cusBill
                    trans.amount=0
                    trans.updated_by=request.user
                    trans.save()

                    return redirect('LabTracksBillPrint/'+str(billdata.id))

                except:
                    cusadd=Customer()
                    if(request.POST['customer']==''):
                        messages.info(request,'please fill customer field')
                    else:
                        cusadd.name=request.POST['customer']
                    if(request.POST['mob']==''):
                        messages.info(request,'please fill mobile number')
                    else:
                        cusadd.phone=request.POST['mob']
                    if(request.POST['email']==''):
                        messages.info(request,'please fill email id')
                    else:
                        cusadd.email=request.POST['email']
                    if(request.POST['address']==''):
                        messages.info(request,'please fill address field')
                    else:
                        cusadd.address=request.POST['address']
                    if(request.POST['age']==''):
                        messages.info(request,'please type age')
                    else:
                        cusadd.age=request.POST['age']
                    if(request.POST['inlineRadioOptionsgender']==''):
                        messages.info(request,'please select gender')
                    else:
                        g=request.POST['inlineRadioOptionsgender']
                        if(g=='option1'):
                            cusadd.gender='M'
                        elif(g=='option2'):
                            cusadd.gender='F'
                        else:
                            cusadd.gender='T'
                    cusadd.updated_by=request.user
                    cusadd.save()

                    cus=Customer.objects.get(id=cusadd.id)

                    cusBill=CustomerBilling()
                    cusBill.customer_id=cus
                    cusBill.customer_name=cus.name
                    cusBill.gender=cus.gender
                    if(child=='option1'):
                        cusBill.is_child='Yes'
                    else:
                        cusBill.is_child='No'
                    cusBill.phone=cus.phone
                    cusBill.email=cus.email
                    cusBill.doctor=docdata
                    cusBill.doc_name=docdata.Doc_Name
                    cusBill.hospital=hosdata
                    cusBill.hosp_name=hosdata.Hospital_Name
                    cusBill.amount=tot
                    cusBill.discount_total=dis
                    cusBill.total_amount=final
                    cusBill.updated_by=request.user
                    cusBill.save()

                    billdata=BillingTestData()
                    billdata.billid=cusBill
                    billdata.test=testdata
                    billdata.discount=disdict
                    billdata.save()

                    trans=fin_transactions()
                    trans.billid=cusBill
                    trans.amount=0
                    trans.updated_by=request.user
                    trans.save()

                    return redirect('LabTracksBillPrint/'+str(billdata.id))
            except:
                messages.info(request,'Not a valid doctor or hospital name!')

    return render(request,'billCreateLabAdmin.html',{'t':tst,'cs':cst,'hs':hospds,'dc':doctds,'billsearch':searchbill})

@login_required(login_url='Login')
def LabTracksBillPrint(request,bid):
    billtest=BillingTestData.objects.get(id=bid)
    cusbill=CustomerBilling.objects.get(id=billtest.billid.id)
    dt=datetime.datetime.now()
    trans=fin_transactions.objects.get(billid=cusbill.id)
    bal=float(cusbill.total_amount)-float(trans.amount)

    if request.method=="POST":
        try:
            amt=float(request.POST['amount'])
            print(amt)
            mode=request.POST['inlineRadioOptions']
            print(mode)
            if(amt==''):
                messages.info(request,'please select a valid amount!!!')
            
            if(mode==''):
                messages.info(request,'please select a valid mode of paymemt!!!')
            elif(mode=='option1'):
                mod='Cash'
            elif(mode=='option2'):
                mod='Card'
            elif(mode=='option3'):
                mod='UPI'
            elif(mode=='option4'):
                mod='Other'
            else:
                mod='unknown'
            com=request.POST['comment']

            trans.payment_mode=mod
            trans.comment=com
            trans.amount=float(trans.amount)+float(amt)
            trans.updated_by=request.user
            trans.save()

            bal=float(cusbill.total_amount)-float(trans.amount)
            return render(request,'billingLabAdmin.html',{'b':billtest,'date':dt,'bill':cusbill,'billsearch':searchbill,'trans':trans,'bal':bal})
        except:
            messages.info(request,'Please Login')
    
    return render(request,'billingLabAdmin.html',{'b':billtest,'date':dt,'bill':cusbill,'billsearch':searchbill,'trans':trans,'bal':bal})

@login_required(login_url='Login')
def pdfprint(request,bid):

    testbillid=BillingTestData.objects.get(id=bid)
    billCustomer=CustomerBilling.objects.get(id=testbillid.billid.id)
    testnames=Test.objects.all()
    trns=fin_transactions.objects.get(billid=billCustomer.id)
    
    idb=billCustomer.id
    nm=billCustomer.customer_name
    ph=billCustomer.phone
    ml=billCustomer.email
    dc=billCustomer.doc_name
    hs=billCustomer.hosp_name
    gen=billCustomer.gender
    dtold=billCustomer.created_at.date()
    chi=billCustomer.is_child
    ag=billCustomer.customer_id.age

    dt=date.today() 
   
    bal=float(billCustomer.total_amount)-float(trns.amount)
    
    return render(request,'billPrint.html',{'testid':testbillid,'billCust':billCustomer,'dt':dt,'testdata':testnames,'billsearch':searchbill,'trans':trns,'tot':bal})

@login_required(login_url='Login')
def removeBill(request,bid):
    try:
        bid=CustomerBilling.objects.get(id=bid)
        bid.delete()
        return redirect('home')
    except:
        messages.info(request,'No query matches this search. please try another')
        return redirect('home')

@login_required(login_url='Login')    
def BillView(request):
    test=Test.objects.all()
    cusB=BillingTestData.objects.all()
    trns=fin_transactions.objects.all()
    return render(request,'ViewBill.html',{'cus':cusB,'trn':trns,'billsearch':searchbill,'tst':test})