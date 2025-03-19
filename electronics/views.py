from django.shortcuts import render
from .models import product
from .forms import productForm
# Create your views here.
def home(request):
    return render(request,'electronics/home.html')

def product_detail(request):
    prod=product.objects.all()
    form = productForm()
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'electronics/product_detail.html',{"prod":prod,"form":form})