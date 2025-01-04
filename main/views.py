from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'result': False,
        'title': 'Home',
        'content': ['Главная страница магазина', 'Страница']
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('<h1>Пока</h1>')