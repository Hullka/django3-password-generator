import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    length_options = list(range(6, 15))  # Создаем список [6, 7, ..., 14]
    return render(request, 'generator/home.html', {'length_options': length_options})

def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-=+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})

def description(request):
    return render(request, 'generator/description.html')