from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Product
# from cart.models import Cart
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def cart(request):
    return render(request, 'store/cart.html')



