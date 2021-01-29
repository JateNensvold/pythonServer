from django.shortcuts import render
from cards.models import CardPost
# Create your views here.
from django.views.decorators.cache import cache_page, cache_control

# Set Cache to public, cache this view for 1 month


@cache_page(86400)
@cache_control(private=False, max_age=2629746)
def card_home(request):
    context = {"path": "cards/img/base/",
               "sports": {
                   "football": {
                       "name": "football"},
                   "basketball": {
                       "name": "basketball"},
                   "baseball": {
                       "name": "baseball"}}}
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
