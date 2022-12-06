from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.shopHome, name='shophome'),
    path('category-list',views.categoryList, name='categorylist'),
    path('product-list',views.productList, name='productlist'),
    path('add-category',views.addCategory, name='addcategory'),
]