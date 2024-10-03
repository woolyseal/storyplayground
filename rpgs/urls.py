from django.urls import path

from . import views

urlpatterns = [
    path("", views.RPGListView.as_view(), name="rpg_list"),
    path("<int:rpg_id>/", views.detail, name="detail"),
]
