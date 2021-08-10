from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='user/register/')
def index(request, slug=None):
    if slug != None:
        category_name = CategoryModel.objects.get(slug=slug)
        products = ProductModel.objects.filter(category=category_name)
        pass
    else:
        products = ProductModel.objects.all()

    category = CategoryModel.objects.all()
    dict_value = {
        'category' : category,
        'products' : products,
    }
    return render(request,'accounts/index.html',dict_value)




@login_required(login_url='user/register/')
def productList(request):
    product_list = ProductModel.objects.all()
    category = CategoryModel.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 10)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    dict_value = {
        'product': product,
        'category': category
    }
    return render(request, 'accounts/search-list.html', dict_value)



@login_required(login_url='user/register/')
def productDetails(request,cat_slug,slug,pk):
    product = ProductModel.objects.get(id=pk)
    dict_value = {
        'product' : product
    }
    return render(request,'accounts/product-detail.html',dict_value)



@login_required(login_url='user/register/')
def search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product = ProductModel.objects.all().filter(Q(name__contains=search)|Q(price__contains=search)|Q(description__contains=search))
        category = CategoryModel.objects.all()
        dict_value = {
            'product' : product,
            'category':category
        }
    return render(request,'accounts/search-list.html',dict_value)


@login_required(login_url='user/register/')
def cart(requset):
    total = 0
    count = 0
    cart_list = None
    cart_item = None
    try:
        cart_list = CartListModel.objects.get(cart_id=cartId(requset))
        cart_item = CartItemModel.objects.filter(cartList=cart_list,active=True)
        for i in cart_item:
            total += (i.product.price*i.quantity)
            count +=i.quantity
    except ObjectDoesNotExist:
        pass
        print("pass")
    dict_value = {
        'cart_item' : cart_item,
        'cart_list' : cart_list,
        'total' : total,
        'count' : count,
     }
    return render(requset,'accounts/cart.html',dict_value)

@login_required(login_url='user/register/')
def cartId(requset):
    cart_id = requset.session.session_key
    if not cart_id:
        cart_id = requset.session_create()
    return cart_id
@login_required(login_url='user/register/')
def addCart(requset,product_id):
    product = ProductModel.objects.get(id = product_id)
    try:
        cart_id = CartListModel.objects.get(cart_id=cartId(requset))
    except CartListModel.DoesNotExist:
        cart_id = CartListModel.objects.create(cart_id=cartId(requset))
        cart_id.save()
    try:
        cart_items = CartItemModel.objects.get(product=product,cartList=cart_id)
        if cart_items.quantity < cart_items.product.stock:
            cart_items.quantity += 1
            cart_items.save()
    except CartItemModel.DoesNotExist:
        cart_items = CartItemModel.objects.create(product=product,quantity=1,cartList=cart_id)
    return redirect('cart')

@login_required(login_url='user/register/')
def addQuantity(requset,item_id):
    cart_id = CartListModel.objects.get(cart_id=cartId(requset))
    product = ProductModel.objects.get(id=item_id)
    cart_item = CartItemModel.objects.get(product=product, cartList=cart_id)
    if cart_item.quantity < product.stock:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = product.stock
        cart_item.save()
    return redirect('cart')

@login_required(login_url='user/register/')
def removeQuantity(requset,item_id):
    cart_id = CartListModel.objects.get(cart_id=cartId(requset))
    product = ProductModel.objects.get(id=item_id)
    cart_item = CartItemModel.objects.get(product=product, cartList=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required(login_url='user/register/')
def deleteCart(request,item_id):
    cart_id = CartListModel.objects.get(cart_id = cartId(request))
    product = ProductModel.objects.get(id=item_id)
    delete_item = CartItemModel.objects.get(product=product,cartList=cart_id)
    delete_item.delete()
    return redirect('cart')
