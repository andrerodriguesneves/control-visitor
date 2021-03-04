from django.shortcuts import render

# Create your views here.
def register_visitor(request):

    context = {}

    return render(request, "registrar_visitante.html", context)