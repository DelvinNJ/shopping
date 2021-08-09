from .models import *
from .views import *

def cartCount(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart_list = CartListModel.objects.get(cart_id=cartId(request))
            cart_item = CartItemModel.objects.filter(cartList=cart_list)
            for i in cart_item:
                item_count += 1

        except:
            item_count =0
        return dict(item_count=item_count)