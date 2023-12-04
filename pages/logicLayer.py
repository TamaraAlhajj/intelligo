import os
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from math import log
from anytree import Node, RenderTree
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def complexity(fn, guess=None):
    """
        INPUT: f(n) \n
        OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
    """

    solution = dict()
    n = symbols('n')

    # turn input into math expression
    try:
        f = parse_expr(fn)
        guess = parse_expr(guess)

        solution["f(n)"] = latex(f)

        # first check if f(n) is bounded by guess(n) as n --> inf
        check = Limit(f/guess, n, oo).doit()
        solution["guess"] = latex(guess)

        if (check.is_constant() and (check != oo)):
            # correct
            solution["guess_solution"] = True
        else:
            # incorrect
            solution["guess_solution"] = False

        # now run analysis on common bounds
        bounds = ['1', 'log(log(n))', 'log(n)', 'log(n)**2', 'sqrt(n)', 'sqrt(n) * log(n)', 'n / log(n)', 'n', 'n*log(log(n))',
                  'n*log(n)', 'n * log(n)**2', 'n**2', 'n**2 * log(n)', 'n**3', 'n**4', '2**n', '3**n']
        math_bounds = [parse_expr(e) for e in bounds]

        omega_index = -1

        # set theta to false unless proven otherwise
        solution["theta"] = False

        for g in math_bounds:
            # check if f(n) is bounded by g(n) as n --> inf
            check = Limit(f/g, n, oo).doit()

            if (check.is_constant() and (check != oo)):
                solution["g(n)"] = latex(g)
                solution["constant"] = check

                if(check > 0):
                    # then by definition f(n) = Theta(g(n))
                    solution["theta"] = True
                    solution["omega"] = latex(g)
                else:
                    if(omega_index == -1):
                        solution["omega"] = '1'
                    else:
                        solution["omega"] = latex(math_bounds[omega_index])

                return (solution)

            omega_index += 1

        solution["g(n)"] = 'n!'
        solution["constant"] = '\\infty'
        solution["omega"] = latex(math_bounds[omega_index])

        return (solution)

    except:
        err_msg = "Error has Occurred"
        return err_msg


def masters_invalid(a, b, k, i):
    """
        INPUT: Master's Arguments
        \nOUTPUT: tuple of True, and error msg if invalid
    """

    try:
        msg = list()
        if(a <= 0):
            msg.append("a must be a positive number, ")
        if(b <= 1):
            msg.append("b must be greater than 1, ")
        if(k < 0):
            msg.append("k must be at least 0, ")
        if(i < 0):
            msg.append("i must be at least 0, ")

        if(len(msg) == 0):
            return(False, "Valid Input")

        return (True, msg)

    except:

        msg = "Invalid Syntax. Please try again."
        return (True, msg)


def masters(a, b, k, i):
    """ 
        INPUT: a >= 0, b > 1, k >= 0, i >= 0 
        \nOUTPUT: Master's Method Analysis of the form
        \n      T(n) = aT(n/b) + Θ(n^k * log(n)^i)
    """

    n = symbols('n')

    invalid_input = masters_invalid(a, b, k, i)

    if(invalid_input[0]):
        msg = invalid_input[1]
        return msg
    else:
        # for math operations
        fn = parse_expr("n**{} * log(n)**{}".format(k, i))
        c_critical = N(log(a, b))

        # for pretty printing functions with latex in view
        if(c_critical == int(c_critical)):
            c_critical = int(c_critical)

        c_latex = "c_{{critical}} = \log_{} {} = {}".format(b, a, c_critical)

        if(k == 0):
            f = ""
        elif(k == 1):
            f = "n"
        else:
            f = "n^{{{}}}".format(k)

        if(i == 0):
            pass
        elif(i == 1):
            f += "log n"
        else:
            f += "log^{{{}}} n".format(i)

        # check for empty string output
        if(f == ""):
            f = "1"

        f = latex(f)

        T = "T(n) = "
        if(a == 1):
            T = latex("T(n) = T(n/{}) + \Theta({})".format(b, f))
        else:
            T = latex("T(n) = {}T(n/{}) + \Theta({})".format(a, b, f))

        if(c_critical > k):
            case = 1
            case_msg = "c_{crit} > k"

            if(c_critical == 0):
                expr = "1"
            elif(c_critical == 1):
                expr = "n"
            else:
                expr = latex("n^{{{}}}").format(c_critical)

            msg = "T(n) = \Theta(n^{{c_{{critical}}}}) = \Theta(n^{{\log_b a}}) = \Theta({})".format(
                expr)

        if(c_critical == k):
            case = 2
            case_msg = "c_{crit} == k"

            if(c_critical == 0):
                expr = latex("log^{{{}}} n".format(i+1))
            elif(c_critical == 1):
                expr = latex("n log^{{{}}} n".format(i+1))
            else:
                expr = latex("n^{{{}}}log^{{{}}} n".format(c_critical, i+1))

            msg = "T(n) = \Theta(n^{{\log_b a}} \log^{{i+1}} n) = \Theta({})".format(expr)

        if(c_critical < k):
            case = 3
            case_msg = "c_{crit} < k"
            fn = latex("n^{{{}}}log^{{{}}} n".format(k, i))

            if(k == 1):
                if(i == 0):
                    msg = "T(n) = \Theta({}) = \Theta({{n}})".format(fn)
                elif(i == 1):
                    msg = "T(n) = \Theta({}) = \Theta({{n log n }})".format(fn)
                else:
                    msg = "T(n) = \Theta({}) = \Theta({{n log^{{i}}n }})".format(
                        fn)
            else:
                if(i == 0):
                    msg = "T(n) = \Theta({}) = \Theta({{n^{{k}}}})".format(fn)
                elif(i == 1):
                    msg = "T(n) = \Theta({}) = \Theta({{n^{{k}} log n }})".format(
                        fn)
                else:
                    msg = "T(n) = \Theta({}) = \Theta({{n^{{k}} log^{{i}}n }})".format(
                        fn)

        solution = {
            "T(n)": T,
            "critical_exponent": c_latex,
            "case_msg": case_msg,
            "case_num": case,
            "msg": latex(msg)
        }

        return (solution)


def generate_tree(a, b, k, i):

    d = dict()
    d[0] = Node("f(n) Root Node")

    invalid_input = masters_invalid(a, b, k, i)[0]

    if(invalid_input):
        a = 2
        height = "\\log_{b} n"
        parent = 0
        total = 1

        for i in range(1, a + 1):
            d[total] = Node("f(n/b) Node: {}".format(total), parent=d[parent])
            total += 1

        parent += 1
        count_children = 0

        for i in range(a**2):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[total] = Node("f(n/b^2) Node: {}".format(total),
                            parent=d[parent])
            total += 1
            count_children += 1

        parent += 1
        count_children = 0

        for i in range(a**3):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[total] = Node("f(n/b^3) Node: {}".format(total),
                            parent=d[parent])
            total += 1
            count_children += 1

    else:

        height = "\\log_{{{}}} n".format(b)
        total = 1
        parent = 0

        for i in range(1, a + 1):
            d[total] = Node(
                "f(n/{}) Node: {}".format(b, total), parent=d[parent])
            total += 1

        parent += 1
        count_children = 0

        for i in range(a**2):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[total] = Node("f(n/{}) Node: {}".format(b **
                                                      2, total), parent=d[parent])
            total += 1
            count_children += 1

        parent += 1
        count_children = 0

        for i in range(a**3):
            if(count_children == a):
                parent += 1
                count_children = 0
            d[total] = Node("f(n/{}) Node: {}".format(b **
                                                      3, total), parent=d[parent])
            total += 1
            count_children += 1

    # render cmd line tree
    with open('./pages/static/tree.txt', 'w') as f:
        for pre, fill, node in RenderTree(d[0]):
            print("%s%s" % (pre, node.name), file=f)
            
    # render new tree image
    if os.path.exists("./pages/static/tree.png"):
        os.remove("./pages/static/tree.png")

    # Create a new graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for node in d.values():
        G.add_node(node.name)
        if node.parent is not None:
            G.add_edge(node.parent.name, node.name)

    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.savefig("./pages/static/tree.png")

    return (height)
