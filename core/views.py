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


def success(request):
    return render(request, 'core/success.html')


def contact(request):
    return render(request, 'core/contact.html')


def tracking_order(request):
    return render(request, 'core/tracking_order.html')
