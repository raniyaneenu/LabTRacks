from django.urls import path
from . import views

urlpatterns=[

    path('LabTracksBilling',views.LabTracksBilling,name='LabTracksBilling'),
    path('LabTracksBillPrint/<int:bid>',views.LabTracksBillPrint,name='LabTracksBillPrint'),
    path('pdf/<str:bid>',views.pdfprint,name='pdf'),
    path('search',views.searching,name='search'),
    path('deleteBill/<str:bid>',views.removeBill,name='deleteBill'),
    path('ViewBill',views.BillView,name='ViewBill')
]