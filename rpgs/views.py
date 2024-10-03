from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the rpgs index.")

def detail(request, rpg_id):
    return HttpResponse("You're looking at rpg %s." % rpg_id)