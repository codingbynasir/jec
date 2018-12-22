from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    police_station=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=200, null=True, blank=True)
    message=models.TextField()
    def __str__(self):
        return self.first_name+' '+self.last_name