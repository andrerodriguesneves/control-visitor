from django import forms
from .models import Visitors


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = "full_name", "cpf", "birth_date", "house_number", "vehicle_plate"