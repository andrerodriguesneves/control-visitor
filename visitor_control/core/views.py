from django.shortcuts import render
from visitor_control.visitors.models import Visitors

# Create your views here.
def index(request):

    all_visitors = Visitors.objects.all

    context = {"name_page": "DashBoard Inicial", "all_visitors": all_visitors}

    return render(request, 'index.html', context)
