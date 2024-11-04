from django.http import HttpResponse
from .models import Products
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem
from .utils import get_or_create_cart
from django.shortcuts import render

def product_list(request):
    products = Products.objects.all()
    product_list = "\n".join(f"{product.name}: ${product.price}" for product in products)
    return HttpResponse(product_list, content_type="text/plain")

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

