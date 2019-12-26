from django.shortcuts import render
from django.views.generic import TemplateView
from pages.forms import ComplexityForm, MastersForm
from pages.models import ComplexityPost, MastersPost
from django.shortcuts import render, redirect
from pages.logicLayer import complexity, masters, generate_tree
import os



class Home(TemplateView):
    template_name = "home.html"


class Notes(TemplateView):
    template_name = "notes.html"


class BigO(TemplateView):
    template_name = "bigO.html"

    def get(self, request):
        form = ComplexityForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ComplexityForm(request.POST)
        if form.is_valid():
            # save data and clean malicious input
            form.save()
            text = form.cleaned_data['post']
            guess = form.cleaned_data['guess']

            # run maths
            solution = complexity(text, guess)

            limit_msg = list()
            more_info = list()

            if(type(solution) == str):
                title = solution
                answer = "\\text{Use python syntax for math expressions.}"
                limit_msg = [
                    "Also make sure your equation is in terms of n.", "Please try again."]
            else:

                f = solution["f(n)"]
                g = solution["g(n)"]
                constant = solution["constant"]
                omega = solution["omega"]

                title = "$$\\text{{Analysis of }} f(n) = {}$$".format(f)
                answer = "f(n) = O({}) ".format(g)

                if(solution["guess_solution"] != False):
                    limit_msg.append(
                        "Your guess was correct! $$f(n) = O({})$$ Shown below is what the analysis tool has returned.".format(solution["guess"]))
                else:
                    limit_msg.append(
                        "Your guess was incorrect. $$f(n) \\neq O({})$$ Shown below is what the analysis tool has returned.".format(solution["guess"]))

                limit_msg.append(
                    "$$\\textbf{Using the Limit}$$ With limits we can deduce the bounds, and thus the run-time, of the function.")
                limit_msg.append(
                    "$$ \lim_{{n \\to +\infty}} \\frac{{{}}}{{{}}} = {}$$".format(f, g, constant))
                limit_msg.append(
                    "Thus, this function has a upper bound of, $$O({})$$.".format(g))

                if(constant is not 0):
                    more_info.append(
                        "Since the limit as n grows to infinity is greater than 0 we can also say,")
                    if(solution["theta"] == True):
                        more_info.append(
                            "$${} \\textbf{{ and }} f(n) = \\Omega({}) \\implies \\Theta({})$$".format(answer, omega, g))
                        more_info.append(
                            "Thus we can say f(n) is tight bound by g(n), meaning the functions grow at approximately the same rate.")
                    else:
                        more_info.append(
                            "$${} \\textbf{{ and }} f(n) = \\Omega({})$$".format(answer, omega))
                        more_info.append(
                            "This means that f(n) grows faster than g(n)")

            # init blank form
            form = ComplexityForm()

            args = {'form': form, 'title': title, 'answer': answer,
                    'lim': limit_msg, 'more': more_info}
            return render(request, self.template_name, args)


class Masters(TemplateView):
    template_name = "masters.html"

    def get(self, request):
        
        form = MastersForm()
        args = {'form': form}

        return render(request, self.template_name, args)

    def post(self, request):

        form = MastersForm(request.POST)

        if form.is_valid():
            # save data and clean malicious input
            form.save()
            try:
                a = int(form.cleaned_data['post_a'])
                b = int(form.cleaned_data['post_b'])
                k = int(form.cleaned_data['post_k'])
                i = int(form.cleaned_data['post_i'])

                # run maths
                solution = masters(a, b, k, i)

                # create tree and function will return respective height
                height = generate_tree(a, b, k, i)

                ans = list()

                if (type(solution) == list):
                    T = "\\textbf{Invalid Input}"

                    for err_msg in solution:
                        print(err_msg)
                        ans.append("\\text{{{}}}".format(err_msg))

                    ans.append("\\text{Please try again.}")
                    tree_msg = "\\text{This is an example tree which shows the first 3 levels of the recursion tree for } a=2."
                    height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(
                        height)

                else:

                    T = solution["T(n)"]
                    critical = solution["critical_exponent"]
                    case_msg = solution["case_msg"]
                    case_num = solution["case_num"]
                    msg = solution["msg"]

                    T = "\\textbf{{Analysis of the recurrence }} {}".format(T)
                    ans.append(critical)
                    ans.append("\\text{{From this we deduce }} {} \\text{{, which then implies we have case }} {}".format(
                        case_msg, case_num))
                    ans.append("\\textbf{{Solution: }} {}".format(msg))
                    tree_msg = "\\text{This is the first 3 levels of the recursion tree for } f(n)."
                    height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(
                        height)

                # init blank form
                form = MastersForm()

                args = {'form': form, 'T': T, 'ans': ans, 'tree_msg': tree_msg,
                        'height': height, 'a': a, 'b': b, 'k': k, 'i': i}

                return render(request, self.template_name, args)

            except:

                T = "\\textbf{Invalid Syntax}"
                ans = ["\\text{Please try again.}"]
                tree_msg = "\\text{This is an } \\textbf{example } \\text{tree which shows the first 3 levels of the recursion tree for } a=2."
                # trigger example from bad input for tree generator
                height = generate_tree(2, 2, 1, 1)
                height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(
                    height)

                # init blank form
                form = MastersForm()

                args = {'form': form, 'T': T, 'ans': ans,
                        'tree_msg': tree_msg, 'height': height}

                return render(request, self.template_name, args)
