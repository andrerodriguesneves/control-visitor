from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VisitorForm
from .models import Visitors

REGISTRADO_SUCESSO = "Visitante registrado com sucesso!"

# Create your views here.
def register_visitor(request):

    form = VisitorForm()

    if request.method == "POST":

        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.registered_by = request.user.porters
            visitor.save()

            messages.success(request, REGISTRADO_SUCESSO)

            return redirect('index')

    context = {"name_page": "Registrar visitante", 
        "form": form}

    return render(request, "registrar_visitante.html", context)

def visitor_information(request, id):

    visitor = get_object_or_404(
        Visitors, id=id
    )
    context = {
        "nome_pagina": "Informações de visitante", 
        "visitante": visitor, 
    }

    return render(request, "info_visitante.html", context)




