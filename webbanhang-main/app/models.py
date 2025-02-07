from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model): #khách hàng
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Product(models.Model): #sản phẩm
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except :
            url = ' '
        return url
class Order(models.Model): 
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_order= models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,null=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)
class OrderItem(models.Model): #sản phẩm đã order
    Product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
class ShippingAddress(models.Model): #thông tin
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address