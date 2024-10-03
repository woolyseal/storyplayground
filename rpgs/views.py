from django.views.generic import ListView, DetailView, CreateView

from .models import RolePlay
from .forms import RolePlayForm

class RPGListView(ListView):
    model = RolePlay
    template_name = "rpg_list.html"
    context_object_name = "rpg_list"


class RolePlayDetail(DetailView):
    model = RolePlay
    template_name = "rpg.html"
    context_object_name = "rpg"


class AddRPGView(CreateView):
    form_class = RolePlayForm
    model = RolePlay
    template_name = "add_rpg.html"
