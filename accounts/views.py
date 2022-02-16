from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages, auth
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from cart.models import Orders
from cart import forms
from accounts.forms import UserForm, ProductForm

# Create your views here.

# for showing login button for admin(by sumit)
# def adminclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return HttpResponseRedirect('adminlogin')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
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
                    # messages.success(request, "You are now logged in.")
                    # return redirect('dashboard')
                    user.save()
                    messages.success(
                        request, 'You are registered successfully')
                    return redirect('userRegister')

        else:
            messages.error(request, 'Password do not match')
            return redirect('userRegister')
    else:
        return render(request, 'accounts/userRegister.html')

# for checking user is user


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
        # else:
        #     messages.success(request, 'You are successfully logged out.')
        #     return redirect('userLogin')
    return redirect('home')


def resetPass(request):
    return render(request, 'accounts/password_reset_form.html')


# def is_customer(user):
#     return user.groups.filter(name='CUSTOMER').exists()

@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('adminDashboard')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('adminlogin')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(username=username, password=password)

    #     if user.is_superuser:
    #         auth.login(request, user)
    #         messages.success(request, 'You are now logged in.')
    #         return redirect('adminDashboard')
    #     else:
    #         messages.error(request, "Invalid login credentials")
    #         return redirect('adminlogin')
    # return render(request, 'accounts/adminlogin.html')

    # if request.user.is_superuser.exists:
    #     return redirect('adminDashboard')
    # else:
    #     return redirect('userDashboard')


@login_required(login_url='afterlogin')
def adminDashboard(request):
    if request.user.is_superuser:
        User = get_user_model()
        usercount = User.objects.all().filter(is_superuser=False).count()
        productcount = models.Product.objects.all().count()
        ordercount = Orders.objects.all().count()
        order = Orders.objects.all()
        mydict = {
            'usercount': usercount,
            'productcount': productcount,
            'ordercount': ordercount,
            'order': order,
        }
        return render(request, 'accounts/adminDashboard.html', mydict)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('adminlogin')
    # return render(request, 'accounts/adminDashboard.html')

# admin view the total product in the dashbaord


@login_required(login_url='adminlogin')
def admin_products_view(request):
    products = models.Product.objects.all()
    return render(request, 'admincontrol/admin_products.html', {'products': products})

# admin add product by clicking on floating button


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

    data = {'order': order}
    # ordered_products=[]
    # ordered_bys=[]
    # for order in orders:
    #     ordered_product=models.Product.objects.all().filter(id=order.product.id)
    #     ordered_by=models.Customer.objects.all().filter(id = order.customer.id)
    #     ordered_products.append(ordered_product)
    #     ordered_bys.append(ordered_by)
    # ,{'data':zip(ordered_products,ordered_bys,orders)}
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

    return render(request,'admincontrol/view_customer.html',{'users':users})

@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    User = get_user_model()
    users=User.objects.get(id=pk)
    users.delete()
    return redirect('view-customer')


@login_required(login_url='userLogin')
def edit_profile_view(request):
    user = models.User.objects.get(id=request.user.id)
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
            # user.set_password(user.password)
            # user.save()
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
    # order = Orders.objects.all().filter(id=user.id)

    data = {
        'order':order
    }
    # ordered_products=[]
    # for order in orders:
    #     ordered_product=models.Product.objects.all().filter(id=order.product.id)
    #     ordered_products.append(ordered_product)
    # {'data': zip(ordered_products, orders)}

    return render(request, 'usercontrol/myorder.html', data)
