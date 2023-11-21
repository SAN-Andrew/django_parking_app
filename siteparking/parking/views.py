from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить cообщение", 'url_name': 'add_msg'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1,
     'title': 'с 20 по 25 ноября 2003',
     'content': '''<h1> Паркинг с 20 по 25 ноября 2003</h1> С 16 ноября парковка начнет работать в открытом режиме, а после 
        переобустройства станет уличной.
        Что изменится:
        тариф станет поминутным мы уберем шлагбаумы — можно будет быстрее заезжать на парковку и выезжать с нее. Об окончании
        переобустройства и старте работы в новом режиме мы сообщим дополнительно — следите за новостями.''',
     'is_published': True},
    {'id': 2,
     'title': 'с 13 по 17 ноября 2003',
     'content': 'Паркинг с 13 по 17 ноября 2003',
     'is_published': False},
    {'id': 3,
     'title': 'с 6 по 10 ноября 2003',
     'content': 'Паркинг с 6 по 10 ноября 2003',
     'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Неделя1'},
    {'id': 2, 'name': 'Неделя2'},
    {'id': 3, 'name': 'Неделя3'},
]
def index(request):
    data = {'title': 'Главная страница - index.html',
            'menu': menu,
            'posts': data_db,
            'cat_selected': 0,
            }
    return render(request, 'parking/index.html', context=data)


def about(request):
    return render(request, 'parking/about.html', {'title': 'О сайте - about.html', 'menu': menu,})

def addmsg(request):
    return HttpResponse("Добавление сообщения")

def login(request):
    return HttpResponse("Авторизация")

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по неделям',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'parking/index.html', context=data)

def show_msg(request, msg_id):
    return HttpResponseNotFound(f'<h1> Отображение сообщения с id = {msg_id} </h1>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена! </h1>')

# def contact(request):
#     return HttpResponse("Контакты")


#
# def registration(request):
#     return HttpResponse('<h1> registration! </h1>')
#     # return render(request, 'home/about.html')
#
# def messages(request, msg_id):
#     return HttpResponse(f'<h1> messages! </h1><p>id: {msg_id}</p>')
#     # return render(request, 'home/about.html')
# def messages_by_slug(request, msg_slug):
#     if request.GET:
#         print(request.GET)
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f'<h1> messages_by_slag! </h1><p>slag: {msg_slug}</p>')
#     # return render(request, 'home/about.html')
#
# def archive(request, year):
#     if year > 2023:
#         # raise Http404() #пример возврата код 404 Нашей страницы когда запрошен не сущетвующий адрес
#         # return redirect('/') #пример редиректа в случае когда страницы нет, на нужную нам страницу с кодом 302
#         # return redirect('/', permanent=True)  # пример редиректа в случае когда страницы нет, на нужную нам страницу с кодом 301
#         # return redirect(index)  # пример редиректа в случае когда страницы нет, на нужную нам страницу по имени страницы с кодом 302
#         # return redirect('msgs')  # пример редиректа в случае когда страницы нет, на нужную нам страницу по псевдониму прописанному в урлс с кодом 302
#         uri = reverse('msgs', args = ('sport',))
#         # return redirect(uri)  # пример редиректа на страницу с параметром в случае когда страницы нет,по псевдониму прописанному в урлс с кодом 302
#         # return HttpResponseRedirect('/') #с кодом 302
#         return HttpResponsePermanentRedirect(uri)  # с кодом 301
#
#     return HttpResponse(f'<h1> archive! </h1><p>year: {year}</p>')
#     # return render(request, 'home/about.html')