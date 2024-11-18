from django.urls import path, include
from .views import product_list, ProductViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('resetPass/', views.reset_password, name='reset password'),
]
