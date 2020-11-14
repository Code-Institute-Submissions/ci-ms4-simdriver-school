from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product, Category
from .models import RaceTrack, Datapack, Week
from user_profiles.models import UserProfile
from .forms import DatapackForm

import datetime
from datetime import timedelta

# Create your views here.


@login_required
def setup_details(request, product_id):

    datapacks = Datapack.objects.filter(product_id__id=product_id)
    profile = UserProfile.objects.get(user=request.user)

    # Validate the user's active datapack
    current_date = datetime.datetime.now().date()
    paid_until = profile.active_pack_date

    if paid_until:
        if paid_until.date() < current_date:
            profile.active_pack_date = None
            profile.active_pack = None
            profile.save()
            messages.info(request, 'Your active datapack has expired!')

    context = {
        'datapacks': datapacks,
        'profile': profile,
    }

    return render(request, 'datapacks/datapacks.html', context)


@login_required
def dataselector(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    imsa = Product.objects.filter(category__name='imsa_series')
    ilms = Product.objects.filter(category__name='ilms')
    imsa_michelin = Product.objects.filter(category__name='imsa_michelin')
    gt3_sprint = Product.objects.filter(category__name='gt3_sprint')
    open_wheeler = Product.objects.filter(category__name='open_wheeler')
    porsche_gt3_cup = Product.objects.filter(category__name='porsche_gt3_cup')
    mazda_mx5 = Product.objects.filter(category__name='mazda-mx5')

    context = {
        'products': products,
        'categories': categories,
        'imsa': imsa,
        'ilms': ilms,
        'imsa_michelin': imsa_michelin,
        'gt3_sprint': gt3_sprint,
        'open_wheeler': open_wheeler,
        'porsche_gt3_cup': porsche_gt3_cup,
        'mazda_mx5': mazda_mx5,

    }
    return render(request, 'datapacks/dataselector.html', context)


@login_required
def add_datapack(request):
    """
    Add new datapack to the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DatapackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added datapack!')
            return redirect(reverse('dataselector'))
        else:
            messages.error(request, 'Failed to add datapack. Please ensure \
                the form is valid.')
    else:
        form = DatapackForm()

    template = 'datapacks/add_datapack.html'
    context = {
        'form': form,
        'on_product_management': True,
    }

    return render(request, template, context)


@login_required
def edit_datapack(request, datapack_id):
    """
    Edit/update a datapack.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admins can do that.')
        return redirect(reverse('home'))

    datapack = get_object_or_404(Datapack, pk=datapack_id)
    if request.method == 'POST':
        form = DatapackForm(request.POST, request.FILES, instance=datapack)
        if form.is_valid():
            form.save()
            messages.success(request, f'The product {datapack.product.name} \
                updated succesfully.')
            return redirect('dataselector')
        else:
            messages.error(request, 'Failed to update datapack.\
                                     Please ensure the form is valid!')
    else:
        form = DatapackForm(instance=datapack)
        messages.info(request, f'You are editing {datapack.product.name}')

    template = 'datapacks/edit_datapack.html'
    context = {
        'form': form,
        'datapack': datapack,
        'on_product_management': True,
    }

    return render(request, template, context)


@login_required
def delete_datapack(request, datapack_id):
    """
    Deleting a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admins can do that.')
        return redirect(reverse('home'))

    datapack = get_object_or_404(Datapack, pk=datapack_id)
    datapack.delete()
    messages.success(request, 'Datapack has been successfully deleted')
    return redirect(reverse('dataselector'))
