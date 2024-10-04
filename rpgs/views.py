from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class RPGAddView(LoginRequiredMixin, CreateView):
    model = RolePlay
    form_class = RolePlayForm
    template_name = "add_rpg.html"
    success_url = '/rpgs/'

    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super(AddRPGView, self).form_valid(form)


class RPGDeleteView(LoginRequiredMixin, DeleteView):
    model = RolePlay
    template_name = "rpg_confirm_delete.html"
    success_url = '/rpgs/'