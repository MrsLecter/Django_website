from django.shortcuts import render

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
    return render(request, 'catalog/add_current_item.html', {'data': id})