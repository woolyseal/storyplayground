from django.urls import path

from . import views

urlpatterns = [
    path("", views.RPGListView.as_view(), name="rpg_list"),
    path("<int:pk>/", views.RolePlayDetail.as_view(), name="rpg"),
    path("addRPG", views.RPGAddView.as_view()),
    path('<pk>/delete/', views.RPGDeleteView.as_view()),
]
