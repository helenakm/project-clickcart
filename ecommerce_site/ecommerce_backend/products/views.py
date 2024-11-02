from django.http import HttpResponse
from .models import Products

def product_list(request):
    products = Products.objects.all()
    product_list = "\n".join(f"{product.name}: ${product.price}" for product in products)
    return HttpResponse(product_list, content_type="text/plain")
