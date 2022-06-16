from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Doctors)
admin.site.register(Doctor_Hospital)
admin.site.register(TestCategory)
admin.site.register(Test)
