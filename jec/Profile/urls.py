from django.urls import path
from . import views
urlpatterns = [
    path('profile/<slug>',views.getBCat.as_view(), name="b_category"),
    path('profile/<slug>',views.getFCat.as_view(), name="f_category")
]