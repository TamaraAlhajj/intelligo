from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.interactive import printing
# printing.init_printing(use_latex=True)
#$O(n\log{}n)$ % regular O
#$\mathcal{O}(n\log{}n)$ % Open at top left

import numpy as np
import matplotlib.pyplot as plt
#import tkinter as Tk

BOUNDS = ['1', 'log(n)', 'n', 'n*log(log(n))', 'n*log(n)', 'n**2', 'n**3', '2**n', 'x!']

def dominator(fn):
    """ 
    INPUT: f(n) \n
    OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
    """
    '''
    step1 - f
    step2 - limit in latex
    step3 - g in latex
    step4 - index in 
    '''

    # turn input into math expression
    n = Symbol('n')
    f = parse_expr(fn)

    step1 = latex(fn)

    # lowest possible bound, constant
    if (f.is_constant()):
        g = parse_expr('1')
        step2 = latex(Limit(f/g, n, oo))
        step3 = latex(g)
        step4 = 0
        return tuple([step1, step2, step3, step4])

    # otherwise check common bounds
    bounds = ['log(n)', 'n', 'n*log(log(n))',
              'n*log(n)', 'n**2', 'n**3', '2**n']
    math_bounds = [parse_expr(e) for e in bounds]

    for g in math_bounds:
        # check if f(n) is bounded by g(n) as n --> inf
        check = Limit(f/g, n, oo).doit()

        if (check.is_constant() and (check != oo)):
            step2 = latex(Limit(f/g, n, oo))
            step3 = latex(g)
            step4 = bounds.index(str(g)) + 1
            return tuple([step1, step2, step3, step4])

    g = parse_expr('n!')
    step2 = latex(Limit(f/g, n, oo))
    step3 = latex(g)
    step4 = 8
    return tuple([step1, step2, step3, step4])


def graph(fn):

    error = False
    x = np.arange(1, 100)
    #y = dominator(fn)[3]
    if(fn == 0):
        y = 1
    elif(fn == 1):
        y =log(x)
    elif(fn == 2):
        y = x
    elif (fn == 3):
        y = x*log(log(x))
    elif (fn == 4):
        y = x*log(x)
    elif (fn == 5):
        y = x**2
    elif (fn == 6):
        y = x**3
    elif (fn == 7):
        y = 2**x
    elif (fn == 8):
        y = factorial(x)
    else:
        error = True

    plt.title("Complexity of {}".format(bounds[fn]))
    plt.xlabel("n number of elements")
    plt.ylabel("Operations")
    plt.plot(x, y)
    plt.show()

    return


def masters(a, b, k, i):

    msg = "Invalid input: "

    if(a < 0):
        msg += "a must be a positive number. "
    elif(b <= 1):
        msg += "b must be greater than 1. "
    elif(k < 0):
        msg += "k must be at least 0. "
    elif(i < 0):
        msg += "i must be at least 0. "
    else:
        msg = ""
    pass


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

#graph(0)
#graph(1)
#graph(2) #works
#graph(3)
#graph(4)
graph(5)
graph(6)
graph(7)
graph(8)

""" graph(range(100), f1)
graph(range(100), f2)
graph(range(100), f3)
graph(range(100), f4)
graph(range(100), f5)
graph(range(100), f6)
graph(range(100), f7)
graph(range(100), f8)
graph(range(100), f9)
graph(range(100), f10) """

""" print(dominator(f1))
print(dominator(f2))
print(dominator(f3))
print(dominator(f4))
print(dominator(f5))
print(dominator(f6))
print(dominator(f7))
print(dominator(f8))
print(dominator(f9))
print(dominator(f10)) """
