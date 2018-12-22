from .models import RulesCategory
from Gallery.models import Category
from Profile.models import FinancialCategory, BusinessCategory

r=RulesCategory.objects.all()
gallery_category=Category.objects.all()
f_category=FinancialCategory.objects.all() #Financial category in f_category
b_category=BusinessCategory.objects.all()