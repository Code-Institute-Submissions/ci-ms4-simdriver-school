from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view to return the users shopping cart """

    return render(request, 'cart/cart.html')
