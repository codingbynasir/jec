from django.urls import path
from . import views
urlpatterns = [
    path('', views.getHome.as_view(), name="index"),
    path('founder', views.getFounder.as_view(), name="founder"),
    path('shareholder/<rank>', views.getShareholder.as_view(), name="shareholder"),
    path('login', views.getLogin.as_view(), name="login"),
    path('act/<slug>', views.lawRules.as_view(), name="act"),
    path('act/pdf/<slug>', views.viewPDF.as_view(), name="pdf")
]