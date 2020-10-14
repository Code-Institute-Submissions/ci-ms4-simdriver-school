from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view to return the users shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = quantity
    messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ Remove a product from the shopping cart """

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
