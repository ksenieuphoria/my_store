from django import forms
from .models import OrderInformation


# Форма, созданная на основе модели
class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderInformation
        fields = ['name', 'email', 'address', 'city']
        help_texts = {'name': (''),
                      'email': (''),
                      'address': (''),
                      'city': (''),}

        widgets = {'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.widgets.EmailInput(attrs={'class': 'form-control'}),
                   'address': forms.widgets.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.widgets.TextInput(attrs={'class': 'form-control'})}