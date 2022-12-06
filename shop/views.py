from django.shortcuts import render

# Create your views here.


def shopHome(request):
    return render(request, 'shop/home.html')


def categoryList(request):
    return render(request, 'shop/category_list.html')


def productList(request):
    return render(request, 'shop/product_list.html')


def addCategory(request):
    return render(request, 'shop/add_category.html')
