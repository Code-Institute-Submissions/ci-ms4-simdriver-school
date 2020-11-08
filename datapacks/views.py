from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product, Category
from .models import RaceTrack, Datapack, Week
from user_profiles.models import UserProfile

# Create your views here.


@login_required
def setup_details(request, product_id):

    setups = Datapack.objects.filter(product_id__id=product_id)
    profile = UserProfile.objects.get(user=request.user)
    
    
    context = {
        'setups': setups,
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
