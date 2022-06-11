from django.shortcuts import render

def basket(request):
    basket_data = request.session.get('basket', {})
    return render(request, 'basket/basket.html', {"data": basket_data})

def complete_purchase(request):
    return render(request, 'basket/complete_purchase.html')