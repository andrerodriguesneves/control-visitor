from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VisitorForm, AuthorizesVisitorForm
from .models import Visitors

from django.http import HttpResponseNotAllowed
from django.utils import timezone


REGISTRADO_SUCESSO = "Visitante registrado com sucesso!"

# Create your views here.
@login_required
def register_visitor(request):

    form = VisitorForm()

    if request.method == "POST":

        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.registered_by = request.user.porters
            visitor.save()

            messages.success(request, REGISTRADO_SUCESSO)

            return redirect("index")

    context = {"name_page": "Registrar visitante", "form": form}

    return render(request, "registrar_visitante.html", context)

@login_required()
def visitor_information(request, id):

    visitor = get_object_or_404(Visitors, id=id)

    form = AuthorizesVisitorForm()

    if request.method == "POST":
        form = AuthorizesVisitorForm(request.POST, instance=visitor)

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.status = "EM_VISITA"
            visitor.authorization_schedule = timezone.now()

            visitor.save()

            form.save()

            messages.success(request, "Entrada do visitante autorizada com sucesso!")

            return redirect("index")

    ## Variaveis que usarei no HTML
    context = {
        "nome_pagina": "Informações de visitante",
        "visitante": visitor,
        "form": form, 
    }

    return render(request, "info_visitante.html", context)

@login_required()
def visitor_finalization(request, id):

    if request.method == "POST":
        visitor = get_object_or_404(Visitors, id=id)

        visitor.status = "FINALIZADO"
        visitor.departure_time = timezone.now()

        visitor.save()

        messages.success(request, "Visita finalizado com sucesso!")

        return redirect("index")
    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )
