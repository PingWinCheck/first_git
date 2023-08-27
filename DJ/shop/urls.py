from django.urls import path

from shop.views import *

urlpatterns = [
    path('', MobileList.as_view(), name='index'),
    path('shop/<slug:slug>/', MobileDetail.as_view(), name='info_mobile'),
    path('add/', MobileCreate.as_view(), name='add')

]