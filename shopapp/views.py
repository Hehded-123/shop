from django.shortcuts import render
from .models import Product

# Create your views here.
def home_page(request):
    items = Product.objects.all()
    return render(request,'index.html', {'items':items})