from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerBilling)
admin.site.register(BillingTestData)
admin.site.register(fin_transactions)
admin.site.register(originalBillTemplates)
admin.site.register(originalResultTemplates)