from django.http import HttpResponse
from django.views.generic import ListView

from .models import RolePlay

class RPGListView(ListView):
    model = RolePlay
    template_name = "rpg_list.html"
    context_object_name = "rpg_list"


def detail(request, rpg_id):
    return HttpResponse("You're looking at rpg %s." % rpg_id)