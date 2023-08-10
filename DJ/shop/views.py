from django.shortcuts import render


from shop.models import Mobile
from django.http import HttpResponseNotFound


def menu_func() -> list[dict[str, str]]:
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'О магазине', 'url': 'about'},
        {'name': 'Регистрация', 'url': 'reg'},
        {'name': 'Войти', 'url': 'enter'},
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
