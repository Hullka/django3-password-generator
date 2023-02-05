from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz') # список букв

    # проверка на верхний регистр
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # проверка на специалные символы
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    
    # проверка на цифры
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    # длина пароля/по умолчанию значения - 12
    length = int(request.GET.get('length', 12)) 

    thepassword = '' # переменная для пароля

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')