from django.shortcuts import render
from .models import Bouquet

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    bouquets = Bouquet.objects.all()
    content = {'bouquets': bouquets}
    return render(request, 'mainapp/bouquets.html', content)


def bouquet(request):
    return render(request, 'mainapp/bouquet.html')


def compositions(request):
    return render(request, 'mainapp/compositions.html')


def wedding(request):
    return render(request, 'mainapp/wedding.html')


def interior(request):
    return render(request, 'mainapp/interior.html')


def blog(request):
    return render(request, 'mainapp/blog.html')


def friends(request):
    return render(request, 'mainapp/friends.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
