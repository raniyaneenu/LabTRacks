from django.urls import path
from . import views

urlpatterns=[
    path('home',views.homepg,name='home'),
    path('nav',views.topmenu,name='nav'),

    path('Hospital',views.addHospitalFun,name='Hospital'),
    path('HospitalList',views.HospitalList,name='HospitalList'),
    path('hospital_edit/<int:hid>',views.EditHospital,name='hospital_edit'),

    path('Doctor',views.AddDoctor,name='Doctor'),
    path('DoctorsList',views.DocView,name='DoctorsList'),
    path('doctor_edit/<int:did>',views.EditDoctor,name='doctor_edit'),

    path('DoctorHosp',views.addDoctorHos,name='DoctorHosp'),

    path('test',views.addTest,name='test'),
    path('TestList',views.TestList,name='TestList'),
    path('test_edit/<int:tid>',views.EditTest,name='test_edit'),

    path('category',views.addCategory,name='category'),
    path('CategoryList',views.CategList,name='CategoryList'),
    path('category_edit/<int:cid>',views.EditCategory,name='category_edit'),
    
]