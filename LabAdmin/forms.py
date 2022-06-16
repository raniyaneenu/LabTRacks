from django import forms

from . models import *

class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields="__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model=TestCategory
        fields="__all__"

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields="__all__"

class DoctorsForm(forms.ModelForm):
    class Meta:
        model=Doctors
        fields="__all__"

class Doctor_HospitalForm(forms.ModelForm):
    class Meta:
        model=Doctor_Hospital
        fields="__all__"