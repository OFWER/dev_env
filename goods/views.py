from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        
    }
    return render(request, 'goods/product.html', context)