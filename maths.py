from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.interactive import printing
# printing.init_printing(use_latex=True)
# $O(n\log{}n)$ % regular O
# $\mathcal{O}(n\log{}n)$ % Open at top left

import numpy as np
import matplotlib.pyplot as plt
#import tkinter as Tk

# All upper bounds for our purposes
BOUNDS = ['1', 'log(n)', 'n', 'n*log(log(n))', 'n*log(n)',
          'n**2', 'n**3', '2**n', 'n!']


def dominator(fn):
    """ 
    INPUT: f(n) \n
    OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
    """
    '''
    step1 - f
    step2 - g
    step3 - limit in latex
    step4 - index in 
    '''

    # turn input into math expression
    n = Symbol('n')
    f = parse_expr(fn)

    # lowest possible bound, constant
    if (f.is_constant()):
        #g = parse_expr('1')
        #lim = latex(Limit(f/g, n, oo))
        g = '1'
        return (g, None)

    # otherwise check common bounds
    bounds = ['log(n)', 'n', 'n*log(log(n))',
              'n*log(n)', 'n**2', 'n**3', '2**n']
    math_bounds = [parse_expr(e) for e in bounds]

    for g in math_bounds:
        # check if f(n) is bounded by g(n) as n --> inf
        check = Limit(f/g, n, oo).doit()

        if (check.is_constant() and (check != oo)):
            #lim = latex(Limit(f/g, n, oo))
            g = str(g)
            return (g, check)

    #g = parse_expr('n!')
    #lim = latex(Limit(f/g, n, oo))
    g = 'n!'
    return (g, None)


def graph(fn):

    x = np.arange(1, 100)
    if(fn == 0):
        y = 1
    elif(fn == 1):
        y = log(x)
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
        print('error')
        return

    plt.title("Complexity of {}".format(str(fn)))
    plt.xlabel("n number of elements")
    plt.ylabel("Operations")
    plt.plot(x, y)
    plt.show()

    return


def masters(a, b, k, i):

    # T(n) = aT(n/b) + f(n) where a >= 1 and b > 1

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
        c_critical = log(a,b)
        fn = parse_expr("n**{} *log(n)**{}".format(k, i))
        print("Recurrence: {}T(n/{}) + {}".format(a, b, fn))
        if(c_critical > k):
            # case 1
            msg = "Case 1: \nT(n) = Θ(n^{})".format(c_critical)
        if(c_critical == k):
            # case 2
            expr = parse_expr("Θ(n**{} * (log(n))**{})".format(c_critical, i+1))
            msg = "Case 2: \nT(n) = {}".format(expr)
        if(c_critical < k):
            # case 3
            expr = parse_expr("Θ(n**{} * (log(n))**{})".format(c_critical, i))
            msg = "Case 3: \nT(n) = {}".format(expr)
        
    return msg


def run():

    testing = True

    while(testing):

        user = input("Press 1 for Big-O tool. Press 2 for Master's Method Tool. \n > ")
        if(user == '1'): 
            f = input("Please input your function using python's math format. \nf(n) = ")
            ans = dominator(f)
            g = ans[0]
            const = ans[1]

            print("-"*20 + "OUTPUT" + "-"*20)
            if(const == None):
                if(g == '1'):
                    print("The function {} is not dependent on n. \nThus, The run time is constant. \nIn other words, f(n) is O({})".format(f, g))
                else:
                    print("The function {} is bound by {}. Thus, f(n) is O({})".format(f, g, g))
            else:
                print("The limit of ({})/{} as n grows to infinity is {}. \nThus, fn is bound by {}. \nIn other words, f(n) is O({})".format(f, g, const, g, g))
        elif(user == '2'):
            tn = input("For the recurrence T(n) = aT(n/b) + Θ(n^k * (logn)^i) \nSeperated by spaces, please input a, b, k, i : ")
            #tn = input("For the recurrence T(n) = aT(n/b) + fn \nSeperated by spaces, please input a, b, fn : ")
            lst = tn.split(' ', 3)
            ints = [int(x) for x in lst]

            msg = masters(ints[0], ints[1], ints[2], ints[3])

            print(msg)
        else:
            print("Invalid input")

        check = input("-"*40 + "\nWant to try again? y/n ")
        if(check == 'n'):
            testing = False

run()

###testing###
"""
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

graph(0)
graph(1)
graph(2) #works
graph(3)
graph(4)
graph(5) #works
graph(6) #works
graph(7) #weird...
graph(8)

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
