from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1500, blank=True, null=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name
