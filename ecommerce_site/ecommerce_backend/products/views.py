from rest_framework import viewsets
from django.http import HttpResponse
from .models import Products
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import SignUpForm
from django import forms
from django.shortcuts import get_object_or_404
from .models import CartItem
from .utils import get_or_create_cart


# def product_list(request):
#     products = Products.objects.all()
#     product_list = "\n".join(f"{product.name}: ${product.price}" for product in products)
#     return HttpResponse(product_list, content_type="text/plain")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

def home(request):
    return render(request, 'home.html', {})


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Invalid username or password"})

    else:
         return render(request, 'login.html', {}) 

def logout_user(request):
       logout(request)
       messages.success(request, ("You have been logged out"))
       return redirect('home') 

def register_user(request):
    
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            if form.errors.get('username'):
                messages.error(request, "Username is already in use.")
                return redirect('register')

            if form.errors.get('email'):
                messages.error(request, "Email is already in use.")    
                return redirect('register')
            else:
                messages.error(request, "Error! Try again")    
                return redirect('register')
    else:        
        return render(request, 'register.html', {'form':form})

def reset_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'reset_password.html')

        try:
            user = User.objects.get(email=email)
            user.password = make_password(new_password)  # Hashes the new password before saving
            user.save()
            messages.success(request, "Password has been reset successfully. You can now log in with your new password.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "No account found with that email address.")
            return render(request, 'reset_password.html')

    return render(request, 'reset_password.html')

def add_to_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        cart =  cart,
        product = product,
    )


    if not created:
        cart_item.quantity = cart_item.quantity + 1
        cart_item.save()


    return redirect('cart_detail')


def cart_detail(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('product')
    total = sum(item.get_subtotal() for item in cart_items)


    context = {
        'cart_items': cart_items,
        'total': total,
    }


    return render(request, 'shop/cart_detail.html', context)


def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)


    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))


        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()


    return redirect('cart_detail')


def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id = item_id)
    cart_item.delete()


    return redirect('cart_detail')


def product_list(request):
    products = Products.objects.all()

    return render(request, 'shop/product_list.html', {'products': products})
