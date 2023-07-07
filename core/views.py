from django.shortcuts import render
from core.models import *
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect

from django.template.loader import render_to_string

# from django.http import HttpResponse


# Create your views here.
def index(request):
    products = Product.objects.filter(product_status="published").order_by("-product_id")

    context = {
        'products': products,
    }
    return render(request, 'core/index.html', context)


# Product
def product_detail_view(request, pid):
    product = Product.objects.get(product_id=pid)
    # Get object or 404

    context = {
        'p': product,
    }

    return render(request, 'core/product-detail.html', context)


def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET["id"])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'id': request.GET['id'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET["id"]) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product

    return JsonResponse({
        'data': request.session['cart_data_obj'],
        'totalcartItems': len(request.session['cart_data_obj'])
    })


def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "core/cart.html", {"cart_data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("core:index")


def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = render_to_string("core/async/cart-list.html", {
                                   "cart_data": request.session['cart_data_obj'],
                                    'totalcartitems': len(request.session['cart_data_obj']),
                                    'cart_total_amount': cart_total_amount})
    # return redirect(request.path)
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})


def update_cart(request):
    product_id = str(request.GET['id'])
    product_qty = request.GET['qty']

    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = render_to_string("core/async/cart-list.html", {"cart_data": request.session['cart_data_obj'],
                                                             'totalcartitems': len(request.session['cart_data_obj']),
                                                             'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

def success(request):
    return render(request, 'core/success.html')


def contact(request):
    return render(request, 'core/contact.html')


def tracking_order(request):
    return render(request, 'core/tracking_order.html')
