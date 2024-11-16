from django.db import models
from datetime import datetime

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1500, blank=True, null=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    product = models.ForeignKey(Products, on_delete=models.CASCADE)  
    rating = models.IntegerField()  
    comment = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'Review by {self.user} for {self.product}'