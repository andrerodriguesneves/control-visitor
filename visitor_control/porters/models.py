from django.db import models

# Create your models here.
class Porters(models.Model):

    users = models.OneToOneField("users.Users", verbose_name="Usuario", on_delete=models.PROTECT)

    full_name = models.CharField(verbose_name="Nome Completo", max_length=200)
    cpf = models.CharField(verbose_name="CPF", max_length=11)    
    phone = models.CharField(verbose_name="Telefone", max_length=11)
    birth_date = models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False )

    class Meta:
        verbose_name = "Porteiro" 
        verbose_name_plural = "Porteiros"
        db_table = "porters"

    def __str__(self):
        return self.full_name
    