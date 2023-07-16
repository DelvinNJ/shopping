# Import
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('category-details/<slug:slug>',views.index,name='index-category'),
    # Product
    path('product-list/',views.productList,name='product-list'),
    path('product-details/<slug:cat_slug>/<slug:slug>/<int:pk>/',views.productDetails,name='product-details'),
    # cart

    path('cart/',views.cart,name='cart'),
    path('add-cart/<int:product_id>',views.addCart,name='add-cart'),
    path('delete-cart-item/<int:item_id>',views.deleteCart,name='delete-cart-item'),

    path('add-quantity/<int:item_id>',views.addQuantity,name='add-quantity'),
    path('remove-quantity/<int:item_id>',views.removeQuantity,name='remove-quantity'),
    #
    path('search/',views.search,name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
