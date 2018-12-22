from django.contrib import admin
from .models import Company, Shareholder, RulesRegulation, RulesCategory
# Register your models here.




admin.site.register(Company)

class ShareholderAdmin(admin.ModelAdmin):
    list_display = ["__str__","designation","rank","email"]
    list_filter = ["designation","rank"]
    search_fields = ["__str__","designation","rank","email"]
    list_display_links = ["__str__","designation"]
    class Meta:
        model=Shareholder

admin.site.register(Shareholder,ShareholderAdmin)

admin.site.register(RulesRegulation)
admin.site.register(RulesCategory)