from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = {"Ryan", "Jacob", "Adam", "Kasey"}
    context = {
        'names': names,
    }
    return render(request, 'home.html', context)
