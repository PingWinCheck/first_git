from django.urls import path

from shop.views import *

urlpatterns = [
    path('', MobileList.as_view(), name='index'),
    path('shop/<slug:slug>/', MobileDetail.as_view(), name='info_mobile'),
    path('add/', MobileCreate.as_view(), name='add'),
    path('shop/<slug:slug>/update/', MobileUpdate.as_view(), name='update'),
    path('shop/<slug:slug>/delete/', MobileDelete.as_view(), name='delete'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('shopping_cart', ShoppingCartListView.as_view(), name='shopping_cart'),
    path('bs', bs, name='bs'),
    path('api/', MobileListAPI.as_view(), name='api'),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
    path('confirm/', Confirm.as_view(), name='confirm'),
    path('confirm/add/', AddAddress.as_view(), name='add_address'),
    # path('userid/', adres, name='userid')
    path('confirm/payment/', Payment.as_view(), name='payment'),
    path('lk/', LK.as_view(), name='lk'),
]