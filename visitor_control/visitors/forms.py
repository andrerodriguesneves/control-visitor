from django import forms
from .models import Visitors


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = "__all__"