from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from cart.models import Orders
from cart import forms
from accounts.forms import UserForm, ProductForm
from django.core.paginator import Paginator

# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('userLogin')
    return render(request, 'accounts/userLogin.html')


def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('userRegister')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('userRegister')
                else:
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    user.save()
                    messages.success(
                        request, 'You are registered successfully')
                    return redirect('userRegister')

        else:
            messages.error(request, 'Password do not match')
            return redirect('userRegister')
    else:
        return render(request, 'accounts/userRegister.html')


@login_required(login_url='userLogin')
def userDashboard(request):
    return render(request, 'accounts/userDashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out.')
        return redirect('userLogin')
    return redirect('home')


def logoutadmin(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            auth.logout(request)
            messages.success(request, 'You are successfully logged out.')
            return redirect('adminlogin')
    return redirect('home')


def resetPass(request):
    return render(request, 'accounts/password_reset_form.html')


@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('adminDashboard')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('adminlogin')



@login_required(login_url='afterlogin')
def adminDashboard(request):
    if request.user.is_superuser:
        User = get_user_model()
        usercount = User.objects.all().filter(is_superuser=False).count()
        productcount = models.Product.objects.all().count()
        ordercount = Orders.objects.all().count()
        # For Pagination
        order = Orders.objects.all()
        paginator = Paginator(order, 10)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        mydict = {
            'usercount': usercount,
            'productcount': productcount,
            'ordercount': ordercount,
            'order': paged_product,
        }
        return render(request, 'accounts/adminDashboard.html', mydict)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('adminlogin')


# admin view the total product in the dashbaord
@login_required(login_url='adminlogin')
def admin_products_view(request):
    products = models.Product.objects.all()
    products=models.Product.objects.order_by('-name')
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'products': paged_product,
    }

    return render(request, 'admincontrol/admin_products.html', data)

# admin add product by clicking on + button
@login_required(login_url='adminlogin')
def admin_add_product_view(request):
    products = models.Product.objects.all()
    productForm = ProductForm()
    if request.method == 'POST':
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request, 'admincontrol/admin_add_products.html', {'productForm': productForm, 'products': products})


@login_required(login_url='adminlogin')
def delete_product_view(request, pk):
    products = models.Product.objects.get(id=pk)
    products.delete()
    return redirect('admin-products')


@login_required(login_url='adminlogin')
def update_product_view(request, pk):
    products = models.Product.objects.get(id=pk)
    productForm = ProductForm(instance=products)
    if request.method == 'POST':
        productForm = ProductForm(
            request.POST, request.FILES, instance=products)
        if productForm.is_valid():
            productForm.save()
            return redirect('admin-products')
    return render(request, 'admincontrol/admin_update_product.html', {'productForm': productForm, 'products': products})


@login_required(login_url='adminlogin')
def admin_view_booking_view(request):
    order = Orders.objects.all()
    paginator = Paginator(order, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'order': paged_product,
    }
    return render(request, 'admincontrol/booking.html', data)


@login_required(login_url='adminlogin')
def update_order_view(request, pk):
    order = Orders.objects.get(id=pk)
    orderForm = forms.OrderForm(instance=order)
    if request.method == 'POST':
        orderForm = forms.OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('admin-view-booking')
    return render(request, 'admincontrol/updateorderstatus.html', {'orderForm': orderForm})

@login_required(login_url='adminlogin')
def delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')


@login_required(login_url='adminlogin')
def view_customer(request):
    User = get_user_model()
    users=User.objects.all().order_by('username').filter(is_superuser=False)
    paginator = Paginator(users, 2)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'users': paged_product,
    }
    return render(request,'admincontrol/view_customer.html',data)

@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    User = get_user_model()
    users=User.objects.get(id=pk)
    users.delete()
    return redirect('view-customer')


@login_required(login_url='userLogin')
def edit_profile_view(request):
    user = User.objects.get(id=request.user.id)
    userForm = UserForm(instance=user)
    mydict = {
        'userForm': userForm,
        'user': user
    }
    if request.method == 'POST':
        userForm = UserForm(request.POST, request.FILES, instance=user)
        if userForm.is_valid():
            user.set_password(user.password)
            userForm.save()
            messages.success(request, "Account Sucessfully Updated")
            return HttpResponseRedirect('userDashboard')

    return render(request, 'usercontrol/edit_profile.html', context=mydict)


@login_required(login_url='userLogin')
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "Account Sucessfully Deleted")
    return redirect('userLogin')


@login_required(login_url='userLogin')
def my_order_view(request, id):
    user = User.objects.get(id=id)
    order = Orders.objects.all()
    paginator = Paginator(order, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'order':paged_product,
    }


    return render(request, 'usercontrol/myorder.html', data)
