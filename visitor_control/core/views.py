from django.shortcuts import render

# Create your views here.
def index(request):

    controle = {"name_page": "DashBoard Inicial"}

    return render(request, 'index.html', controle)
