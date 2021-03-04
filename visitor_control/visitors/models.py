from django.db import models

# Create your models here.

class Visitors(models.Model):

    full_name = models.CharField(verbose_name="Nome Completo", max_length=200)
    cpf = models.CharField(verbose_name="CPF", max_length=11)        
    birth_date = models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False )
    house_number = models.PositiveSmallIntegerField(verbose_name="Número da casa a ser visitada" )
    vehicle_plate = models.CharField(verbose_name="Placa do veiculo", max_length=7, blank=True, null=True)
    arrival_time = models.DateTimeField(verbose_name="Horario chegada", auto_now=True)
    departure_time = models.DateTimeField(verbose_name="Horario Saida", auto_now=False, blank=True, null=True)
    authorization_schedule = models.DateTimeField(verbose_name="Horario Autorizacao", auto_now=False, blank=True, null=True)
    
    responsible_resident = models.CharField(verbose_name="Morador responsavel por autorizar a entrada do visitante", 
        max_length=200, blank=True)

    registered_by = models.ForeignKey("porters.Porters", 
        verbose_name="Porteiro responsavel pelo registro", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitors"

    def __str__(self):
        return self.full_name
    