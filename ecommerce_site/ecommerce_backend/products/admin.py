from django.contrib import admin
from .models import Products
from .models import Review

admin.site.register(Products)
admin.site.register(Review)
