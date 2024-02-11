from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name='home'),
    path('list_products/', views.list_products, name='list_product'),
    path('detail_products/<pk>', views.detail_product, name='detail_product')

]