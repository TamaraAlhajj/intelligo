from django import forms


class ComplexityForm(forms.Form):
    post = forms.CharField(required=True)
