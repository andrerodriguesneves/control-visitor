from django.db import models

# Create your models here.

class Visitors(models.Model):

    VISITING_STATUS = [
        ("AGUARDANDO", "Aguardando autorização" ),
        ("EM_VISITA", "Em visita" ),
        ("FINALIZADO", "Visita finalizada")
    ]

    status = models.CharField(verbose_name="Status", max_length=10, choices=VISITING_STATUS, default="AGUARDANDO")

    full_name = models.CharField(verbose_name="Nome Completo", max_length=200)
    cpf = models.CharField(verbose_name="CPF", max_length=11)        
    birth_date = models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False )
    house_number = models.PositiveSmallIntegerField(verbose_name="Número da casa a ser visitada" )
    vehicle_plate = models.CharField(verbose_name="Placa do veiculo", max_length=7, blank=True, null=True)
    arrival_time = models.DateTimeField(verbose_name="Horario chegada", auto_now_add=True)
    departure_time = models.DateTimeField(verbose_name="Horario Saida", auto_now=False, blank=True, null=True)
    authorization_schedule = models.DateTimeField(verbose_name="Horario Autorizacao", auto_now=False, blank=True, null=True)
    
    responsible_resident = models.CharField(verbose_name="Morador responsavel por autorizar a entrada do visitante", 
        max_length=200, blank=True)

    registered_by = models.ForeignKey("porters.Porters", 
        verbose_name="Porteiro responsavel pelo registro", on_delete=models.PROTECT)


    def get_departure_time(self):
        if self.departure_time:
            return self.departure_time

        return "Horário de saída não registrado!"

    def get_authorization_schedule(self):
        if self.authorization_schedule:
            return self.authorization_schedule

        return "Visitante aguardando autorização."

    def get_responsible_resident(self):
        if self.responsible_resident:
            return self.responsible_resident

        return "Visitante aguardando liberação."

    def get_vehicle_plate(self):
        if self.vehicle_plate:
            return self.vehicle_plate

        return "Veículo não registrado!"

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

            return cpf


    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitors"

    def __str__(self):
        return self.full_name
