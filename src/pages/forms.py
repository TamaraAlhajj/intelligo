from django import forms
from pages.models import ComplexityPost, MastersPost


class ComplexityForm(forms.ModelForm):
    post = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-sm-7',
            'placeholder': 'Input Equation...'
        }
    ))

    # required for Model Forms
    class Meta:
        model = ComplexityPost
        # comma makes this a tuple and thus immutable
        fields = ('post', )


class MastersForm(forms.ModelForm):
    post = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-sm-7',
            'placeholder': 'Input Equation...'
        }
    ))
