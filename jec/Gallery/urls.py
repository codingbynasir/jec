from django.urls import path
from . import views
urlpatterns = [
    path('<slug>', views.getCategory.as_view(), name="category"),
]