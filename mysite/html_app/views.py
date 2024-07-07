from django.http import HttpResponse
from django.shortcuts import render
from tools import tools

def index(request):
    map_func = tools.listing_method("./my_modules")
    context = { "map_func":map_func }
    return render(request, 'index.html', context)