from django.shortcuts import render
from core.models import *

# from django.http import HttpResponse


# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'core/index.html', context)

def product_detail_view(request, pid):
    product = Product.objects.get(product_id=pid)
    # Get object or 404

    context = {
        'p': product,
    }

    return render(request, 'core/product-detail.html', context)

def success(request):

    return render(request, 'core/success.html')


def contact(request):
    return render(request, 'core/contact.html')


def tracking_order(request):
    return render(request, 'core/tracking_order.html')
