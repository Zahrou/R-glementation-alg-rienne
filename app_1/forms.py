from django import forms


class basicform(forms.Form):
    Numero_text = forms.CharField(required=False)
    Date_signature = forms.DateField(required=False)
    Mots_cles = forms.CharField(required=False)
