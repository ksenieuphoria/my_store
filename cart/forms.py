from django import forms

choices = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label="Количество", choices=choices, coerce=int, widget=forms.Select(attrs={'type': 'quantity', 'class': 'form-select', 'id': 'autoSizingSelect'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

