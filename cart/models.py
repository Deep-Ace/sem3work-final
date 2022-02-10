from django.db import models
from accounts.models import Product

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __unicode__(self):
        return self.product


# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
#     amount_paid = models.CharField(max_length=100)
#     create_at = models.DateTimeField(auto_now_add=True)
#     email = models.CharField(max_length=50)
#     address = models.CharField(max_length=500)
#     mobile = models.CharField(max_length=20)    
#     def __str__(self) -> str:
#         return self.payment_id


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')
    order_date = models.DateField(auto_now_add=True)

# class Order(models.Model):
#     status_choice = (
#         ('New', 'New'),
#         ('Accepted', 'Accepted'),
#         ('Completed', 'Completed'),
#         ('Cancelled', 'Cancelled'),
#     )
#     name = models.CharField(max_length=40)
#     product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
#     price = models.PositiveIntegerField()
#     status = models.CharField(choices=status_choice, max_length=40)

#     def sub_total(self):
#         return self.quantity * self.product.price

#     def __str__(self):
#         return self.name
