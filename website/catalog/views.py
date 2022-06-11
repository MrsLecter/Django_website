import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

def add_current_item(request, id):
    if request.method == 'POST':
        basket_data = request.session.get('basket',{}) 
        item_count = basket_data.get(str(id), 0)
        basket_data[str(id)] = item_count + 1
        request.session['basket'] = basket_data
        return render(request, 'catalog/add_current_item.html', {'data':id, 'basket': basket_data})
    else:
        data = json.loads(request.data)
        productId = data['productId']
        action = data['action']
        print('action: ' + action)
        print('product: ' + productId)
        return JsonResponse('Item was added', safe=False)

@login_required(login_url='/login/')
def checkout(request):
    basket_data = request.session.get('basket', {})
    user_id = request.user.id
    basket_data.update({"user_id": user_id})
    website.data_access.postToDatabase(basket_data)
    return redirect("/")
    