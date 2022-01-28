from django.shortcuts import render
from accounts import models

# Create your views here.
def home(request):
    # For showing featured Products
    featured_product = models.Product.objects.filter(is_featured=True)
    products=models.Product.objects.all()
    data = {
        'products':products,
        'featured_product': featured_product,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')