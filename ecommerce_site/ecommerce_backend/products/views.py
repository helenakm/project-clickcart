from rest_framework import viewsets
from django.http import HttpResponse
from .models import Products, Review
from .serializers import ProductSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import SignUpForm
from django import forms
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import Customer
from .models import CartItem
from .utils import get_or_create_cart
=======
from .models import *
>>>>>>> 8ddff5f4ec70939875a78f0054130d21ee359295

def product_list(request):
    products = Products.objects.all()

    # Filtering
    name_filter = request.GET.get('name')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    if name_filter:
        products = products.filter(name__icontains=name_filter)

    if price_min:
        products = products.filter(price__gte=price_min)

    if price_max:
        products = products.filter(price__lte=price_max)

    # Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by in ['name', '-name', 'price', '-price']:
        products = products.order_by(sort_by)

    return render(request, 'product_list.html', {'products': products})

class ProductViewSet(viewsets.ModelViewSet):
   queryset = Products.objects.all()
   serializer_class = ProductSerializer

def product_view(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'product_view.html', {'product': product})

def home(request):
    categories = Category.objects.all()  # Get all categories from the database
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'category_detail.html', {'category': category, 'products': products})

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

def get_reviews(request, product_id):
    reviews = Review.objects.filter(product_id=product_id)
    reviews_list = [
        {
            "id": review.id,
            "user": f"{review.user.first_name} {review.user.last_name}",
            "rating": review.rating,
            "comment": review.comment,
            "created_at": review.created_at,
        }
        for review in reviews
    ]
    return JsonResponse(reviews_list, safe=False)

# Add a review for a product
@login_required
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        data = request.POST
        product_id = data.get("product_id")
        rating = data.get("rating")
        comment = data.get("comment")

        if not product_id or not rating or not comment:
            return JsonResponse({"error": "All fields are required"}, status=400)

        customer = request.user.customer    
        product = get_object_or_404(Products, id=product_id)
        

        review = Review.objects.create(
            user=customer, product=product, rating=rating, comment=comment
        )
        review.save()
        messages.success(request, "Review added successfully!")
        

        product = get_object_or_404(Products, id=product_id)
        return render(request, 'product_view.html', {'product': product})

def search_bar(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        # Query the Products model for name or description containing the search term
        searched_products = Products.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        # Check if no products were found
        if not searched_products.exists():
            messages.warning(request, "No products found. Please try again.")
        return render(request, "search_bar.html", {'searched': searched_products, 'query': searched})
    else:
        return render(request, "search_bar.html", {})
    
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

    return render(request, 'cart_detail.html', context)

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

    return render(request, 'product_list.html', {'products': products})
