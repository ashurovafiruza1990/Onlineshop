from django.shortcuts import render
from .models import Product,Card

# Create your views here.
def index(request):
    products=Product.objects.all()
    
    return render(request, 'base.html', {'products': products})

def card(req,pk):
    product = Product.objects.get(pk=pk)
    cardItems = Card.objects.create(product=product, number=1, total=product.price).save()
    
    return render('card.html', {'cardItems': cardItems})