from django.shortcuts import render
from .forms import VisitorForm

# Create your views here.
def register_visitor(request):

    form = VisitorForm()

    context = {"name_page": "Registrar visitante", 
        "form": form}

    return render(request, "registrar_visitante.html", context)