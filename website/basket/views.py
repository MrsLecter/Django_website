from django.shortcuts import render

def basket(request):
    return render(request, 'basket/basket.html')

def complete_purchase(request):
    return render(request, 'basket/complete_purchase.html')