from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def bigO(fn):
    """
        INPUT: f(n) \n
        OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
    """

    soln = []

    n = symbols('n')

    # turn input into math expression
    f = parse_expr(fn)
    soln.append(fn)

    # lowest possible bound, constant
    if (f.is_constant()):
        g = '1'
        soln.append(g)
        soln.append(g)
        return (soln)

    # otherwise check common bounds
    bounds = ['log(n)', 'log(n)**2', 'sqrt(n)', 'n', 'n*log(log(n))',
              'n*log(n)', 'n**2', 'n**3', '2**n', '3**n']
    math_bounds = [parse_expr(e) for e in bounds]

    for g in math_bounds:
        # check if f(n) is bounded by g(n) as n --> inf
        check = Limit(f/g, n, oo).doit()

        if (check.is_constant() and (check != oo)):
            g = str(g)
            soln.append(g)
            soln.append(check)
            return (soln)

    g = 'n!'
    soln.append(g)
    soln.append(check)
    return (soln)


def masters(a, b, k, i):
    """ 
        INPUT: a >= 0, b > 1, k >= 0, i >= 0 
        \nOUTPUT: Master's Method Analysis of the form
        \n      T(n) = aT(n/b) + Θ(n^k * (logn)^i)
    """

    n = symbols('n')

    msg = "Invalid input: "
    if(a < 0 or None):
        msg += "a must be a positive number. "
    elif(b <= 1 or None):
        msg += "b must be greater than 1. "
    elif(k < 0 or None):
        msg += "k must be at least 0. "
    elif(i < 0 or None):
        msg += "i must be at least 0. "
    else:
        c_critical = log(a, b)
        print("The critical exponent is \n=log(# of subproblems)/log(relative problem size) \n= log(a)/log(b) \n= log base b of a \n= {}".format(c_critical))
        fn = parse_expr("n**{} * log(n)**{}".format(k, i))
        print("Recurrence: is {}T(n/{}) + {}".format(a, b, fn))

        if(c_critical > k):
            # case 1
            msg = "Case 1: \nT(n) = Θ(n^{})".format(c_critical)
        if(c_critical == k):
            # case 2
            expr = parse_expr(
                "Θ(n**{} * (log(n))**{})".format(c_critical, i+1))
            msg = "Case 2: \nT(n) = {}".format(expr)
        if(c_critical < k):
            # case 3
            msg = "Case 3: \nT(n) = {}".format(fn)

    return msg
