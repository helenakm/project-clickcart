from rest_framework import viewsets
from django.http import HttpResponse
from .models import Products
from .serializers import ProductSerializer

def product_list(request):
    products = Products.objects.all()
    product_list = "\n".join(f"{product.name}: ${product.price}" for product in products)
    return HttpResponse(product_list, content_type="text/plain")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer