from django.views.generic import ListView, DetailView

from .models import RolePlay

class RPGListView(ListView):
    model = RolePlay
    template_name = "rpg_list.html"
    context_object_name = "rpg_list"


class RolePlayDetail(DetailView):
    model = RolePlay
    template_name = "rpg.html"
    context_object_name = "rpg"