from django import forms

choices = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label="Количество", choices=choices, coerce=int, widget=forms.Select(attrs={'type': 'quantity', 'class': 'form-select', 'id': 'autoSizingSelect'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


# x = [(i, str(i)) for i in range(1, 2)]


# class CartAdd_Form(forms.Form):
#     quantity = forms.TypedChoiceField(label="", choices=x, coerce=int, widget=forms.HiddenInput)
#     # quantity = forms.TypedChoiceField(label="", choices=x, coerce=int, widget=forms.HiddenInput)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

