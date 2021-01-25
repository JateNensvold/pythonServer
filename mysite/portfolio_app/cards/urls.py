from django.urls import path
from cards import views


urlpatterns = [
    path("", views.card_home, name="card_home"),
    path("search", views.card_index, name="card_index"),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
]
