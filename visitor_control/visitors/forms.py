from django import forms
from .models import Visitors


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = ["full_name", "cpf", "birth_date", "house_number", "vehicle_plate"]

        error_messages = {
            "full_name": {
                "required": "O nome completo do visitante é obrigatório para o registro!"
            },
            "cpf": {
                "required": "O CPF do visitante é obrigatório para o registro! !"
            },
            "birth_date": {
                "required": "A data de nascimento é obrigatória para o registro!",
                "invalid": "Por favor, informa um formato válido para a data de nascimento! (dd/mm/aaaa)"
            },
            "house_number": {
                "required": "Informe o número da casa!"
            }
        }