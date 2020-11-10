from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

import datetime
from datetime import timedelta

from checkout.models import Order


@login_required
def user_profile(request):
    """ Page for user profiles """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    # Validate the user's active datapack
    current_date = datetime.datetime.now().date()   
    paid_until = profile.active_pack_date

    if paid_until:
        if paid_until.date() < current_date:
            profile.active_pack_date = None
            profile.active_pack = None
            profile.save()
            messages.warning(request, 'Your active datapack has expired!')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    To show the order history on profile page
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.warning(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
