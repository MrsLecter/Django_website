from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact_page, name='contact_page'),
    path('category/', views.category, name='category'),
    path('category/<str:category>', views.current_category, name='current_category'),
    path('item/<int:id>', views.current_item, name='current_item'),
    path('item/<int:id>/add', views.add_current_item, name='add_current_item'),
]