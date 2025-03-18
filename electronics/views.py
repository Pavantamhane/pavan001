from django.shortcuts import render
from .models import product
# Create your views here.
def home(request):
    return render(request,'electronics/home.html')

def product_detail(request):
    prod=product.objects.all()
    return render(request,'electronics/product_detail.html',{"prod":prod})