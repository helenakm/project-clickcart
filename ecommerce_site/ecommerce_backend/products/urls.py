from django.urls import path, include
from .views import product_list, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('api/', include(router.urls)),
]
