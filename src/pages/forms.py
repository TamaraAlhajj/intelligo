from django import forms
from pages.models import ComplexityPost, MastersPost
from django.core.validators import validate_slug


class ComplexityForm(forms.ModelForm):
    post = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-12',
            'placeholder': 'Input Equation...'
        }
    ))
    guess = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-12 mt-2',
            'placeholder': 'Optional: Guess the answer...'
        }
    ))

    # required for Model Forms
    class Meta:
        model = ComplexityPost
        # comma makes this a tuple and thus immutable
        fields = ('post', 'guess')


class MastersForm(forms.ModelForm):
    post_a = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a positive number...'
        }
    ))
    post_b = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a number greater than 1...'
        }
    ))
    post_k = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a positive number...'
        }
    ))
    post_i = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a positive number...'
        }
    ))

    class Meta:
        model = MastersPost
        fields = ('post_a', 'post_b', 'post_k', 'post_i')
