from django.shortcuts import render


from shop.models import Mobile
from django.http import HttpResponseNotFound


# Create your views here.
def index(request):
    read_db = Mobile.objects.all()
    menu = [
        {'name': 'Главная', 'url': 'index'},
        {'name': 'О магазине', 'url': 'about'},
        {'name': 'Регистрация', 'url': 'reg'},
        {'name': 'Войти', 'url': 'enter'},
]
    return render(request, 'index.html', {'db': read_db, 'name': 'Главная', 'menu': menu})


def desc(request, slug):
    rdb = Mobile.objects.get(slug=slug)

    return render(request, 'descriptions.html', {'data': rdb, 'name': rdb.name})


def PageNotFound(request, exception):
    return render(request, 'error404.html', {'name': 'error'})

def about(requst):
    return render(requst,'error404.html')
def reg(requst):
    pass
def enter(requst):
    pass