from sympy import *
from sympy.parsing.sympy_parser import parse_expr

from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from graphviz import Source, render

import string


def bigO(fn):
    """
        INPUT: f(n) \n
        OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
    """

    soln = []

    n = symbols('n')

    # turn input into math expression
    f = parse_expr(fn)
    soln.append(latex(f))

    # otherwise check common bounds
    bounds = ['1', 'log(n)', 'log(n)**2', 'sqrt(n)', 'n', 'n*log(log(n))',
              'n*log(n)', 'n**2', 'n**3', '2**n', '3**n']
    math_bounds = [parse_expr(e) for e in bounds]

    omega = -1
    theta = False
    for g in math_bounds:
        # check if f(n) is bounded by g(n) as n --> inf
        check = Limit(f/g, n, oo).doit()

        if (check.is_constant() and (check != oo)):
            g = latex(g)
            soln.append(g)
            soln.append(check)

            if(check > 0):
                theta = True
                omega = g
            else:
                if(omega == -1):
                    omega = '1'
                else:
                    omega = latex(math_bounds[omega])

            soln.append(omega)
            soln.append(theta)
            return (soln)

        omega += 1

    g = 'n!'
    soln.append(g)
    soln.append('\\infty')

    omega = latex(math_bounds[omega])
    soln.append(omega)
    soln.append(theta)

    return (soln)


def masters_invalid(a, b, k, i):
    """
        INPUT: Master's Arguments
        \nOUTPUT: tuple of True, and error msg if invalid
    """
    msg = "According to the Masters Theorem\n"
    if(a < 0 or None):
        msg += "a must be a positive number, "
    elif(b <= 1 or None):
        msg += "b must be greater than 1, "
    elif(k < 0 or None):
        msg += "k must be at least 0, "
    elif(i < 0 or None):
        msg += "i must be at least 0, "
    else:
        return (False, "Valid input")

    return (True, msg)


def masters(a, b, k, i):
    """ 
        INPUT: a >= 0, b > 1, k >= 0, i >= 0 
        \nOUTPUT: Master's Method Analysis of the form
        \n      T(n) = aT(n/b) + Θ(n^k * log(n)^i)
    """

    n = symbols('n')

    valid = masters_invalid(a, b, k, i)

    if(valid[0]):

        msg = valid[1]
        return msg

    else:

        # for math operations
        fn = parse_expr("n**{} * log(n)**{}".format(k, i))
        c_critical = log(a, b)

        # for pretty printing functions with latex in view
        crit_latex = "c_{{critical}} = \log_{} {} = {}".format(b, a, c_critical)
        f = latex("n^{{{}}}log^{{{}}} n".format(k, i))
        T = latex("T(n) = {}T(n/{}) + \Theta({})".format(a, b, f))
        

        if(c_critical > k):
            case = 1
            explain = "c_{crit} > k"
            expr = latex("n^{{{}}}").format(crit_latex)
            msg = "T(n) = \Theta(n^{{c_{{critical}}}}) = \Theta(n^{{\log_b a}}) = \Theta({})".format(expr)

        if(c_critical == k):
            case = 2
            explain = "c_{crit} == k"

            if(c_critical == 0):
                expr = latex("log^{{{}}} n".format(i+1))
            elif(c_critical == 1):
                expr = latex("n log^{{{}}} n".format(i+1))
            else:
                expr = latex("n^{{{}}}log^{{{}}} n".format(c_critical, i+1))

            msg = "T(n) = \Theta(n^{{\log_b a}} \log^{{i+1}} n) = \Theta({})".format(expr)

        if(c_critical < k):
            case = 3
            explain = "c_{crit} < k"
            fn = latex("n^{{{}}}log^{{{}}} n".format(k, i))

            if(k == 1):
                if(i == 0):
                    msg = "T(n) = \Theta({{n}}) = \Theta({})".format(fn)
                elif(i == 1):
                    msg = "T(n) = \Theta({{n log n }}) = \Theta({})".format(fn)
                else:
                    msg = "T(n) = \Theta({{n log^{{i}}n }}) = \Theta({})".format(fn)
            else:
                if(i == 0):
                    msg = "T(n) = \Theta({{n^{{k}}}}) = \Theta({})".format(fn)
                elif(i == 1):
                    msg = "T(n) = \Theta({{n^{{k}} log n }}) = \Theta({})".format(fn)
                else:
                    msg = "T(n) = \Theta({{n^{{k}} log^{{i}}n }}) = \Theta({})".format(fn)

        return (T, crit_latex, explain, case, latex(msg))


def generate_tree(a, b, k, i):

    d = dict()
    d[0] = Node("f(n) Root Node")

    if(masters_invalid(a, b, k, i)[0]):
        height = "\\log_{b} n"
        parent = 0

        for i in range(1, a+1):
            d[i] = Node("f(n/b) Node: {}".format(i), parent=d[parent])

        parent += 1
        count_children = 0
        for i in range(a+1, a**2 + 1):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[i] = Node("f(n/b^2) Node: {}".format(i), parent=d[parent])
            count_children += 1

        for i in range(1, a**3 + 1):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[i] = Node("f(n/b^3) Node: {}".format(i), parent=d[parent])
            count_children += 1

    else:

        height = "\\log_{{{}}} n".format(b)
        total = 1
        parent = 0

        for i in range(1, a + 1):
            d[total] = Node("f(n/{}) Node: {}".format(b, total), parent=d[parent])
            total += 1

        parent += 1
        count_children = 0

        for i in range(a**2):
            if(count_children == a):
                print(parent)
                parent += 1
                count_children = 0
            d[total] = Node("f(n/{}) Node: {}".format(b**2, total), parent=d[parent])
            total += 1
            count_children += 1

        parent += 1
        count_children = 0
        
        for i in range(a**3):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[total] = Node("f(n/{}) Node: {}".format(b**3, total), parent=d[parent])
            total += 1
            count_children += 1

    for pre, fill, node in RenderTree(d[0]):
        print("%s%s" % (pre, node.name))

    DotExporter(d[0]).to_picture("./pages/static/images/tree.png")

    return (height)
