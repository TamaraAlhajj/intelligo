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
            elif(check == 0):
                omega = g
            elif(omega is not -1):
                omega = bounds[omega]
            else:
                omega = '1'

            soln.append(omega)
            soln.append(theta)
            return (soln)

        omega += 1

    g = 'n!'
    soln.append(g)
    soln.append(check)

    omega = bounds[omega]
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
        \n      T(n) = aT(n/b) + Θ(n^k * (logn)^i)
    """

    n = symbols('n')

    valid = masters_invalid(a, b, k, i)

    if(valid[0]):

        msg = valid[1]
        return msg

    else:
        c_critical = log(a, b)

        crit_latex = "= \log_{} {}".format(b, a)

        fn = parse_expr("n**{} * log(n)**{}".format(k, i))
        T = latex("T(n) = {}T(n/{}) + \Theta({})".format(a, b, fn))

        if(c_critical > k):
            case = 1
            explain = "c_{crit} > k"
            tree = "leaf-heavy"
            msg = "T(n) = \Theta(n^{{\log_b a}}) = \Theta({})".format(
                c_critical)

        if(c_critical == k):
            case = 2
            explain = "c_{crit} == k"
            tree = "balanced"

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
            tree = "root-heavy"

            if(k == 1):
                if(i == 0):
                    msg = "T(n) = \Theta({{n}}) = \Theta({})".format(latex(fn))
                elif(i == 1):
                    msg = "T(n) = \Theta({{n log n }}) = \Theta({})".format(
                        latex(fn))
                else:
                    msg = "T(n) = \Theta({{n log^{{i}}n }}) = \Theta({})".format(
                        latex(fn))
            else:
                if(i == 0):
                    msg = "T(n) = \Theta({{n^{{k}}}}) = \Theta({})".format(
                        latex(fn))
                elif(i == 1):
                    msg = "T(n) = \Theta({{n^{{k}} log n }}) = \Theta({})".format(
                        latex(fn))
                else:
                    msg = "T(n) = \Theta({{n^{{k}} log^{{i}}n }}) = \Theta({})".format(
                        latex(fn))

        return (T, crit_latex, c_critical, explain, case, latex(msg), tree)


def generate_nodes(a, b, k, i):

    level2 = list()
    level3 = list()
    level4 = list()  # pseudo-leaves

    if(masters_invalid(a, b, k, i)[0]):
        height = "\\log_{b} n"
        level2.append("\\frac{{n}}{{a}}")
        level3.append("\\frac{{n}}{{a**2}}")
        level4.append("\\frac{{n}}{{a**3}} \\newline")
    else:
        height = "\\log_{{{}}} n".format(b)

        for i in range(1, a+1):
            level2.append("\\frac{{n}}{{{}}}".format(a))
        for i in range(1, a**2 + 1):
            level3.append("\\frac{{n}}{{{}}}".format(a**2))
        for i in range(1, a**3 + 1):
            level4.append("\\frac{{n}}{{{}}} \\newline...".format(a**3))
    
    return (height, level2, level3, level4)
