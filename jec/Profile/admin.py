from django.contrib import admin
from .models import BusinessCategory, FinancialCategory, BusinessProfile, FinancialProfile
# Register your models here.
admin.site.register(BusinessCategory)
admin.site.register(FinancialCategory)
admin.site.register(FinancialProfile)
admin.site.register(BusinessProfile)