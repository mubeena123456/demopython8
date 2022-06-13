from django.db import models

# Create your models here.
class Customer_details(models.Model):
    customer_name=models.CharField(max_length=250)
    phone_no=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    address = models.TextField()
    district = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    chocolate = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.customer_name)