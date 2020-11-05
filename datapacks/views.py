from django.shortcuts import render
from products.models import Product, Category


# Create your views here.


def datapacks(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'datapacks/datapacks.html', context)


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