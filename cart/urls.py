from django.urls import path
from cart import views


urlpatterns = [
    # path('add-to-cart/<int:pk>', views.add_to_cart_view, name='add-to-cart'),
    # path('cart', views.cart_view,name='cart'),
    # path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    
    path('cart', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_cart, name="add-to-cart"),
    path('remove_item/<int:cart_item_id>/', views.remove_cart_item, name="remove_item"),
]
