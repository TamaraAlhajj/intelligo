from sympy import *
from sympy.parsing.sympy_parser import parse_expr

n = symbols('n')

def dominator(fn):
    """ 
    INPUT: f(n) \n
    OUTPUT: O(g(n)) such that f(n) is bounded by g(n)
    """

    # turn input into math expression
    f = parse_expr(fn)

    # lowest possible bound, constant
    if (f.is_constant()):
        g = '1'
        return (g, None)

    # otherwise check common bounds
    bounds = ['log(n)', 'log(n)**2', 'sqrt(n)', 'n', 'n*log(log(n))',
              'n*log(n)', 'n**2', 'n**3', '2**n', '3**n']
    math_bounds = [parse_expr(e) for e in bounds]

    for g in math_bounds:
        # check if f(n) is bounded by g(n) as n --> inf
        check = Limit(f/g, n, oo).doit()

        if (check.is_constant() and (check != oo)):
            g = str(g)
            print("check is {}".format(check))
            return (g, check)

    g = 'n!'

    return (g, None)


def masters(a, b, k, i):

    # T(n) = aT(n/b) + f(n) where a >= 1 and b > 1

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


def run():

    testing = True

    while(testing):

        user = input(
            "Press 1 for Big-O tool. Press 2 for Master's Method Tool. \n > ")
        if(user == '1'):
            try:
                f = input(
                    "Please input your function using python's math format. \nf(n) = ")
                ans = dominator(f)
                g = ans[0]
                const = ans[1]

                print("-"*20 + "OUTPUT" + "-"*20)
                if(const == None):
                    if(g == '1'):
                        print(
                            "The function {} is not dependent on n. \nThus, The run time is constant. \nIn other words, f(n) is O({})".format(f, g))
                    else:
                        print(
                            "The function {} is bound by {}. Thus, f(n) is O({})".format(f, g, g))
                else:
                    if(const > 0):
                        print(
                            "The limit of ({})/{} as n grows to infinity is {}. \nThus, fn is tight bound by {}. \nIn other words, f(n) is Θ({})".format(f, g, const, g, g))
                    else:
                        print(
                            "The limit of ({})/{} as n grows to infinity is {}. \nThus, fn is bound by {}. \nIn other words, f(n) is O({})".format(f, g, const, g, g))
            except SyntaxError:
                print("Invalid Syntax given for f(n)")
        elif(user == '2'):
            try:
                print("For the recurrence T(n) = aT(n/b) + Θ(n^k * (logn)^i)")
                tn = input("Seperated by spaces, please input a, b, k, i : ")
                lst = tn.split(' ', 3)
                ints = [int(x) for x in lst]

                msg = masters(ints[0], ints[1], ints[2], ints[3])

                print(msg)
            except IndexError:
                print("Invalid input of variables for T(n)")
        else:
            print("Invalid input")

        check = input("-"*40 + "\nWant to try again? y/n ")
        if(check == 'n'):
            testing = False


run()

###testing###
"""
f = '4'
f = '5+10'
f = 'n'
f = '2*n + 4'
f = 'n*(n+1)/2'
f = 'log(n) + n**2'
f = 'n*log(log(n))'
f = '2**n + n*log(n) + 4*n + 52'
f = '3**n - 2'
f = 'n**3 + log(n) - 5'
f = 'n!'
"""
