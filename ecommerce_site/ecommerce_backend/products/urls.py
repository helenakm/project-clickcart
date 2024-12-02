from django.urls import path, include
from .views import product_list ,ProductViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from . import views
from .models import Cart

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_view, name='product_view'),
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('resetPass/', views.reset_password, name='reset password'),
    path('reviews/<int:product_id>/', views.get_reviews, name='get_reviews'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('search_bar/', views.search_bar, name='search_bar'),
<<<<<<< HEAD
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),

]
=======
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
>>>>>>> 8ddff5f4ec70939875a78f0054130d21ee359295
