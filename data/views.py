from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'judul': 'Halaman Dashboard',
        'menu': 'home'
    }
    return render(request, 'dashboard.html', context)


def products(request):
    context = {
        'judul': 'Halaman Produk',
        'menu': 'products'
    }
    return render(request, 'products.html', context)


def custumer(request):
    context = {
        'judul': 'Halaman Customer',
        'menu': 'custumer'
    }
    return render(request, 'customer.html', context)
