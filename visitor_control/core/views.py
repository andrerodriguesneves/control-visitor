from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from visitor_control.visitors.models import Visitors

from django.utils import timezone

# Create your views here.

@login_required
def index(request):

    all_visitors = Visitors.objects.order_by(
        "-arrival_time"
    )

    visitors_waiting = all_visitors.filter(status="AGUARDANDO")
    visits_in_progress = all_visitors.filter(status="EM_VISITA")
    visits_closed = all_visitors.filter(status="FINALIZADO")

    current_time = timezone.now()

    current_month = current_time.month

    visitors_month = all_visitors.filter(arrival_time__month=current_month)



    ## Variaveis que usarei no HTML!!!!!
    context = {
        "name_page": "DashBoard Inicial",
        "all_visitors": all_visitors,
        "visitantes_aguardando": visitors_waiting.count(),
        "visitas_em_andamento": visits_in_progress.count(),
        "visitas_encerradas": visits_closed.count(),
        "visitas_totais": visitors_month.count(),

    }

    return render(request, 'index.html', context)
