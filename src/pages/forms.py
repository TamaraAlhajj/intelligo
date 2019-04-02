from django import forms
from pages.models import ComplexityPost, MastersPost


class ComplexityForm(forms.ModelForm):
    post = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-12',
            'placeholder': 'Input Equation...'
        }
    ))

    # required for Model Forms
    class Meta:
        model = ComplexityPost
        # comma makes this a tuple and thus immutable
        fields = ('post', )


class MastersForm(forms.ModelForm):
    post_a = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a positive number...'
        }
    ))
    post_b = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a number greater than 1...'
        }
    ))
    post_k = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a positive number...'
        }
    ))
    post_i = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-sm-7 aria-label="Large" aria-describedby="inputGroup-sizing-lg"',
            'placeholder': 'Input a positive number...'
        }
    ))

    # required for Model Forms
    class Meta:
        model = MastersPost
        # comma makes this a tuple and thus immutable
        fields = ('post_a', 'post_b', 'post_k', 'post_i' )
