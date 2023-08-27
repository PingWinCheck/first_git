from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from shop.models import Mobile
from .forms import *
from django.http import HttpResponseNotFound


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


    # if request.method == 'POST':
    #     delmobile = DelMobile(request.POST)
    #     if delmobile.is_valid():
    #         print(delmobile.cleaned_data)
    #         print(delmobile.cleaned_data['delmobile'])
    #         Mobile.objects.filter(name=delmobile.cleaned_data['delmobile']).delete()
    #         return redirect('dvd')
    # else:
    #     delmobile = DelMobile()

    # if request.method == 'POST':
    #     delmobile = DelMobile(request.POST)
    #     if delmobile.is_valid():
    #         Mobile.objects.filter(name=delmobile.cleaned_data['name']).delete()
    #         print(delmobile.cleaned_data)
    #         return redirect('dvd')
    # else:
    #     delmobile = DelMobile()

    context = {
        'form': form,
        # 'formdel': delmobile,
    }
    return render(request, 'learn.html', context=context)


class MobileList(ListView):
    model = Mobile
    ordering = '-quantity'
    template_name = 'telephone.html'
    context_object_name = 'mobiles'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная - телефоны'
        return context

    # def get(self, request):
    #     find = request.GET['find']
    #     # self.model.filter(name=find)
    #     return reverse('index')

class MobileDetail(DetailView):
    model = Mobile
    template_name = 'desc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['mobile'].name
        return context


class MobileCreate(CreateView):
    form_class = MobileForm
    template_name = 'learn.html'
