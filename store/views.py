from django.shortcuts import render
from accounts import models

# Create your views here.
def store(request):
    products=models.Product.objects.all()
    # products=models.Product.objects.filter(available='In Stock')
    data = {
        'products':products,
    }
    return render(request, 'store/store.html',data)

# def about(request):
#     return render(request, 'pages/about.html')
