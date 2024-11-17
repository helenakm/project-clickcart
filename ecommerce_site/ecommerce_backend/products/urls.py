from django.urls import path, include
from .views import product_list
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from . import views

router = DefaultRouter()


urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_view, name='product_view'),
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('resetPass/', views.reset_password, name='reset password'),
    path('search_bar/', views.search_bar, name='search_bar'),
    path('reviews/<int:product_id>/', views.get_reviews, name='get_reviews'),
    path('reviews/add/', views.add_review, name='add_review'),
]
