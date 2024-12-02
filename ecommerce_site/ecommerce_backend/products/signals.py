from django.contrib.auth.signals import user_logged_in
from .models import Cart

def assign_cart_to_user(request, user, **kwargs):
    session_cart_id = request.session.get('cart_id')

    if session_cart_id:
        session_cart = Cart.objects.get(id = session_cart_id)
       
        try:
            user_cart = Cart.objects.get(user = user)
        except Cart.DoesNotExist:
            session_cart.user = user
            session_cart.save()


user_logged_in.connect(assign_cart_to_user)