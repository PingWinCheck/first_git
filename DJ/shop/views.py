from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from rest_framework import generics

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from shop.models import Mobile
from .forms import *
from django.http import HttpResponseNotFound

from .serializers import MobileSerializer
from .utils import ContexteMixin


def menu_func() -> list[dict[str, str]]:
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'О магазине', 'url': 'about'},
        {'name': 'Регистрация', 'url': 'reg'},
        {'name': 'Войти', 'url': 'dvd'},
    ]
    return menu


def index(request, menu=menu_func):
    read_db = Mobile.objects.all()
    return render(request, 'index.html', {'db': read_db, 'title': 'Главная', 'menu': menu})


def PageNotFound(request, exception):
    return render(request, 'error404.html', {'name': 'error'})


def about(request, menu=menu_func):
    context = {
        'title': 'О сайте',
        'menu': menu,

    }
    return render(request, 'about.html', context=context)


def reg(request):
    pass


def enter(request):
    pass


def desc(request, slug):
    rdb = Mobile.objects.get(slug=slug)
    return render(request, 'descriptions.html', {'data': rdb, 'name': rdb.name})


def dvd(request):
    mobile = Mobile.objects.all().order_by('-quantity')
    if request.GET:
        name = request.GET['find']
        mobile = mobile.filter(firm__name__icontains=name) | mobile.filter(name__icontains=name)
    context = {
        'title': 'Телефоны',
        'mobiles': mobile,
    }
    return render(request, 'telephone.html', context=context)

def desc_dvd(request, slug):
    context = {
        'mobile': Mobile.objects.get(slug=slug)
    }
    return render(request, 'desc.html', context=context)


def learn(request):
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dvd')
    else:
        form = ModelForm()

    context = {
        'form': form,
        # 'formdel': delmobile,
    }
    return render(request, 'form.html', context=context)


class MobileList(ContexteMixin, ListView):
    model = Mobile
    ordering = '-quantity'
    template_name = 'telephone.html'
    context_object_name = 'mobiles'


    def get_queryset(self):

        q = self.request.GET.get('find')
        if q:
            return self.model.objects.filter(name__icontains=q) | self.model.objects.filter(firm__name__icontains=q)
        return self.model.objects.all().order_by('-quantity')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Главная - телефоны'
        return {**context, **self.add_context()}

    def post(self, request, *args, **kwargs):
        if 'add_cart' in request.POST:
            ShoppingCart.objects.create(user=request.user, mobile_id=request.POST['add_cart'])

        elif 'plus_cart' in request.POST:
            s = ShoppingCart.objects.get(mobile_id=request.POST['plus_cart'], user=request.user)
            s.quantity += 1
            s.save()
        elif 'minus_cart' in request.POST:
            s = ShoppingCart.objects.get(mobile_id=request.POST['minus_cart'], user=request.user)
            s.quantity -= 1
            s.save()
            if s.quantity == 0:
                s.delete()
        elif 'like' in request.POST:
            if not request.session.get('like'):
                request.session['like'] = []
            if not int(request.POST['like']) in request.session['like']:
                request.session['like'] = request.session['like'] + [int(request.POST['like'])]
            else:
                request.session.modified = True
                request.session['like'].remove(int(request.POST['like']))
        return redirect('/')


class MobileDetail(ContexteMixin, DetailView):
    model = Mobile
    template_name = 'desc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['mobile'].name
        return context | self.add_context()


class MobileCreate(CreateView):
    form_class = MobileForm
    template_name = 'form.html'


class MobileUpdate(UpdateView):
    model = Mobile
    template_name = 'form.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение - ' + context['mobile'].name
        return context


class MobileDelete(DeleteView):
    model = Mobile
    template_name = 'form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить - ' + context['mobile'].name
        return context


class RegisterUser(CreateView):
    model = User
    # fields = '__all__'
    form_class = UserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'form.html'
    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


class ShoppingCartListView(ContexteMixin, ListView):
    model = ShoppingCart
    template_name = 'shopping_cart.html'
    context_object_name = 'shopping_cart'

    def get_queryset(self):
        result = self.model.objects.filter(user=self.request.user)
        # print(f'queryS -  {result}')
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # print(f'context -  {context}')
        price = 0
        for i in self.get_queryset():
            price += i.mobile.price * i.quantity
        context['sum'] = price
        return context | self.add_context(title='Корзина')

    def post(self, request, *args, **kwargs):
        if 'plus_cart' in request.POST:
            s = ShoppingCart.objects.get(user=request.user, pk=request.POST['plus_cart'])
            s.quantity += 1
            s.save()
        elif 'minus_cart' in self.request.POST:
            s = ShoppingCart.objects.get(user=request.user, pk=request.POST['minus_cart'])
            s.quantity -= 1
            s.save()
            if s.quantity == 0:
                s.delete()

        return redirect('shopping_cart')

def bs(request):
    return render(request, 'bs.html')


class MobileListAPI(generics.ListAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class FavouritesView(ListView):
    model = Mobile
    context_object_name = 'mobiles'
    template_name = 'favourites.html'


    def get_queryset(self):
        qs = []
        for i in self.request.session['like']:
            qs.append(Mobile.objects.get(pk=i))
        return qs

    def post(self, request, *args, **kwargs):
        self.request.session.modified = True
        self.request.session['like'].remove(int(request.POST['like']))
        return redirect('/favourites/')


class Confirm(ListView):
    model = Address
    template_name = 'confirm.html'
    context_object_name = 'address'


    def post(self, request, *args, **kwargs):
        if 'adr' in request.POST:
            request.session['address'] = int(request.POST['adr'])
            print(request.session.items())
            return redirect('payment')
        return redirect('/confirm')


class AddAddress(CreateView):
    model = Address
    template_name = 'add_address.html'
    fields = ('city', 'street', 'home', 'flat')
    success_url = reverse_lazy('confirm')
    # initial = {'user': 1}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)





def adres(request):
    user = request.user.pk
    ad = AdresForm(initial={'user': user})
    # ad['user'] = user

    context = {'userid': user,
               'form': ad,
    }

    return render(request, 'adres.html', context=context)


class Payment(TemplateView):
    template_name = 'payment.html'

    def post(self, request):
        if int(self.request.POST['paymethod']) < 3:
            return redirect('/')
        return redirect('/confirm/payment/')


class LK(ListView):
    template_name = 'lk.html'
    context_object_name = 'address'

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['carts'] = ShoppingCart.objects.filter(user=self.request.user)

        return context

    def post(self, request):
        Address.objects.filter(user=self.request.user).update(checked=False)
        Address.objects.filter(pk=self.request.POST['adr']).update(checked=True)
        return redirect(reverse_lazy('lk'))
