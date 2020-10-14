from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view to return the users shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
