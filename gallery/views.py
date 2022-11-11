from django.shortcuts import render
from .models import card

# Create your views here.


def index(request):
    return render(request, 'index.html')


def upload(request):
    alert = False
    if request.method == 'POST':
        tittle = request.POST.get("tittle")
        pic = request.FILES["file"]
        card(tittle=tittle, pics=pic).save()
        alert = True
    context = {
        'alert': alert,
    }
    return render(request, 'index.html', context)


def gallery(request):
    cards = card.objects.all()
    length = 'avialable'
    if len(cards) == 0:
        length = 'empty'
    context = {
        'cards': cards,
        'length': length
    }
    return render(request, 'gallery.html', context)
