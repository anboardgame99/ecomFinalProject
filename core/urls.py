from django.urls import path
from core.views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = "home"

urlpatterns = [
    path("", index, name='index'),
    path('success', success, name='success'),
    path('contact', contact, name='contact'),
    path('tracking', tracking_order, name='tracking_order'),

    path("product/<pid>/", product_detail_view, name="product-detail"),

    # Cart
    path('add-to-cart/', add_to_cart, name="add-to-cart"),
    path('cart/', cart_view, name="cart"),
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    path("update-cart/", update_cart, name="update-cart"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)