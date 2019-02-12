from django.db import models

from sympy import *
from mpmath import *
from sympy.parsing.sympy_parser import parse_expr


class Maths(models.Model):

    #fn = models.TextField()

    def dominator(fn):
        """ 
        INPUT: f(n)
        OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
        """
        # turn input into math expression
        n = symbols('n')
        f = parse_expr(fn)

        # lowest possible bound
        if (f.is_constant()):
            return 'O(1)'

        # otherwise check common bounds
        bounds = ['log(n)', 'n', 'n*log(log(n))',
                  'n*log(n)', 'n**2', 'n**3', '2**n']
        math_bounds = [parse_expr(e) for e in bounds]

        for g in math_bounds:
            # check if f(n) is bounded by g(n) as n --> inf
            check = Limit(f/g, n, oo).doit()
            if (check.is_constant() and (check != oo)):
                return 'O({})'.format(g)
        return 'O(n!)'


""" 
###testing###

f1 = '4'
f2 = '5+10'
f3 = 'n'
f4 = '2*n + 4'
f5 = 'n*(n+1)/2'
f6 = 'log(n) + n**2'
f7 = 'n*log(log(n))'
f8 = '2**n + n*log(n) + 4*n + 52'
f9 = 'n**3 + log(n) - 5'
f10 = 'n!'

print(dominator(f1))
print(dominator(f2))
print(dominator(f3))
print(dominator(f4))
print(dominator(f5))
print(dominator(f6))
print(dominator(f7))
print(dominator(f8))
print(dominator(f9))
print(dominator(f10))
 """
