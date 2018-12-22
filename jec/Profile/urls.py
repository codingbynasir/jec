from django.urls import path
from . import views
urlpatterns = [
    path('<slug>',views.getBCat.as_view(), name="b_category"),
    path('<slug>',views.getFCat.as_view(), name="f_category")
]