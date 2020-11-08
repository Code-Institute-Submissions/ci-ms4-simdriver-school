from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view to return the users shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Checking items in cart and offers the better deal
    if cart == {'30': 1}:
        messages.warning(request, f'You already have Gold Package in your cart. \
            Gold Package gives you access to all the cars / datapacks')
    elif cart != {}:
        messages.info(request, 'You tried to add an another datapack to your cart. \
            Why not upgrade your cart to the Gold Package (£9.99) to access all the cars for \
            the same amount of money?')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def upgrade_to_gold(request):
    """
    Upgrading the user's cart to Gold Package
    """
        
    try:
        if 'cart' in request.session:
            del request.session['cart']

            request.session['cart'] = {'30': 1}
            messages.success(request, 'Your package was successfuly upgraded to Gold Package!')
        else:
            request.session['cart'] = {'30': 1}
            messages.success(request, 'Your package was successfuly upgraded to Gold Package!')
    except:
        messages.error(request, 'Upgrade failed. Try again later.')

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove a product from the shopping cart """

    try:
        product = get_object_or_404(Product, pk=item_id)       
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.error(request, f'Removed {product.name} from your cart')
        
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
