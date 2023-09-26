from shop.models import *


class ContexteMixin:
    def add_context(self, **kwargs):
        context = kwargs
        carts = ShoppingCart.objects.filter(user=self.request.user)
        cart_count = 0
        cart_id = []
        for cart in carts:
            cart_id.append(cart.mobile.pk)
            cart_count += cart.quantity
        context['carts'] = cart_id
        context['cart_count'] = cart_count
        context['count_favourites'] = len(self.request.session['like'])
        return context
