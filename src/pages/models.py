from django.db import models
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class ComplexityPost(models.Model):
    post = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)


class MastersPost(models.Model):
    post_a = models.CharField(max_length=5)
    post_b = models.CharField(max_length=5)
    post_k = models.CharField(max_length=5)
    post_i = models.CharField(max_length=5, default=0)

    date = models.DateTimeField(auto_now_add=True)
