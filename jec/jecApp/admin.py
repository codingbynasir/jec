from django.contrib import admin
from .models import Company, Shareholder, RulesRegulation, RulesCategory, Designation, Rank
# Register your models here.




admin.site.register(Company)

class ShareholderAdmin(admin.ModelAdmin):
    list_display = ["__str__","design","email"]
    search_fields = ["__str__","email"]
    list_display_links = ["__str__"]
    class Meta:
        model=Shareholder

admin.site.register(Shareholder,ShareholderAdmin)

admin.site.register(RulesRegulation)
admin.site.register(RulesCategory)
admin.site.register(Rank)
admin.site.register(Designation)