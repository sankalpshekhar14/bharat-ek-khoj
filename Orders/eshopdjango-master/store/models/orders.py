from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address1 = models.CharField(max_length=50, default='', blank=True, null=True)
    address2 = models.CharField(max_length=50, default='', blank=True, null=True)
    phone = models.CharField(max_length=50, default='', blank=True, null=True)
    state= models.CharField(max_length=50, default='', blank=True, null=True)
    pincode = models.IntegerField(default=1, null=True)
    quantity = models.IntegerField(default=1)
    city = models.CharField(max_length=50, default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

