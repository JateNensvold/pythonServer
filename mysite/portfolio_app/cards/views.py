from django.shortcuts import render
from cards.models import CardPost
# Create your views here.


def card_home(request):
    context = {"sports": {
        "football": {
            "image": "cards/img/base/football.jpg"},
        "basketball": {
            "image": "cards/img/base/basketball.jpg"},
        "baseball": {
            "image": "cards/img/base/baseball.jpg"}}}
    return render(request, "card_home.html", context)


def search_view(request):
    pass


def card_index(request):
    cards = CardPost.objects.all()
    context = {"cards": cards}
    return render(request, "card_index.html", context)


def card_detail(request, pk):
    card = CardPost.objects.get(pk=pk)
    context = {"card": card}

    return render(request, "project_detail.html", context)
