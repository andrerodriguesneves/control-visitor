from django.shortcuts import render
from .forms import VisitorForm

# Create your views here.
def register_visitor(request):

    form = VisitorForm()

    if request.method == "POST":

        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.registered_by = request.user.porters
            visitor.save()

            return redirect("index")

    context = {"name_page": "Registrar visitante", 
        "form": form}

    return render(request, "registrar_visitante.html", context)