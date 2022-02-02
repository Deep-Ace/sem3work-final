from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem, Product
from accounts import forms, models

# Create your views here.


def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        # for item in request.POST:
        #     key = item
        #     value = request.POST[key]

        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:
            messages.success(request, "Item Already In Cart")
            return redirect('store')
            
            # cart_item = CartItem.objects.get()
            # cart_item.quantity += 1
            # cart_item.save()
        else:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                user=current_user,
            )
            cart_item.save()
            messages.success(request, "Item Added In Cart")

        return redirect('store')

def cart(request, total=0.0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.all().filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
    except:
        # print("except")
        pass

    context = {
        "cart_items": cart_items,
    }

    return render(request, 'store/cart.html', context)


def remove_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()

    return redirect('cart')