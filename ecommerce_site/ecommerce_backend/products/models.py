from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length = 60)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    description = models.CharField(max_length = 250, blank = True, null = True)
    image = models.ImageField(upload_to = 'uploads/products/', blank = True, null = True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username if self.user else 'Guest'}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete = models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        'Products',
        on_delete = models.CASCADE
    )

    quantity = models.PositiveIntegerField(default = 1)

    def get_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"