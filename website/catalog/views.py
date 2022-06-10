import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
import website.data_access

def index(request):
    return render(request, 'index.html')

def contact_page(request):
    return render(request, 'contact_page.html')

def category(request):
    return render(request, 'catalog/category.html')

def current_category(request, category):
    return render(request, 'catalog/category.html', {'data': category})

def current_item(request, id):
    return render(request, 'catalog/current_item.html', {'data': id})

def add_current_item(request, item_id):
    if request.method == 'POST':
        basket_data = request.session.get('basket',{}) 
        item_count = basket_data.get(str(item_id), 0)
        basket_data[str(item_id)] = item_count + 1
        request.session['basket'] = basket_data
        return redirect("/basket")
    else:
        data = json.loads(request.data)
        productId = data['productId']
        action = data['action']
        print('action: ' + action)
        print('product: ' + productId)
        return JsonResponse('Item was added', safe=False)

def checkout(request):
    basket_data = request.session.get('basket', {})
    user_id = request.user.id
    basket_data.update({"user_id": user_id})
    website.data_access.postToDatabase(basket_data, "purchases")
    return redirect("/")
    