from django.shortcuts import render
from django.views.generic import TemplateView
from pages.forms import ComplexityForm, MastersForm
from pages.models import ComplexityPost, MastersPost
from django.shortcuts import render, redirect
from pages.logicLayer import bigO, masters, generate_nodes


class Home(TemplateView):
    template_name = "home.html"


class Info(TemplateView):
    template_name = "info.html"


class BigO(TemplateView):
    template_name = "bigO.html"

    def get(self, request):
        form = ComplexityForm()
        #post = ComplexityPost.objects.all().order_by('-date')[0]

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ComplexityForm(request.POST)
        if form.is_valid():
            # save data and clean malicious input
            form.save()
            text = form.cleaned_data['post']

            # run maths
            soln = bigO(text)
            lim = list()
            more = list()
            f = "$$\\text{{Analysis of }} f(n) = {}$$".format(soln[0])
            g = "f(n) = O({}) ".format(soln[1])
            const = soln[2]
            omega = soln[3]

            if(soln[1] == 1):
                lim.append("The function {} is not dependent on n. Thus, The run time is constant.".format(soln[0]))
                lim.append("Thus we can also say it is tight bound, meaning $$f(n) = \\Theta(1)$$")
            
            lim.append("Using limits we can deduce the bounds, and thus the run-time, of the function.")
            lim.append("$$ \lim_{{n \\to +\infty}} \\frac{{{}}}{{{}}} = {}$$".format(soln[0], soln[1], const))
            lim.append("Thus, this function has a upper bound of, $${}$$.".format(g))
            lim.append("This is the worst case run-time.")
            
            if(const is not 0):
                more.append("The best case run-time of this function can also be inferred from the limit we have just found!")
                more.append("Since the limit as n grows to infinity is a constant greater than 0 we can say,")
                if(soln[4]):
                    more.append("$${} \\textbf{{ and }} f(n) = \\Omega({}) \\implies \\Theta({})$$".format(g, omega, g))
                    more.append("Thus we can say f(n) is tight bound by g(n), meaning the functions grow at approximately the same rate.")
                else:
                    more.append("$${} \\textbf{{and}} f(n) = \\Omega({})$$".format(g, omega))
                    more.append("This means that f(n) grows faster than g(n)")
            
            # init blank form
            form = ComplexityForm()

        args = {'form': form, 'f': f, 'g': g, 'lim': lim, 'more': more}
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
            a = int(form.cleaned_data['post_a'])
            b = int(form.cleaned_data['post_b'])
            k = int(form.cleaned_data['post_k'])
            i = int(form.cleaned_data['post_i'])

            # run maths
            soln = masters(a, b, k, i)
            ans = list()

            # create tree
            tree = generate_nodes(a, b, k, i)
            height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(tree[0])
            nodes2 = tree[1]
            nodes3 = tree[2]
            leaves = tree[3]

            if (type(soln) == str):
                T = "\\textbf{Invalid Input}"

                ans.append("\\text{{{}}}".format(soln))
                ans.append("\\text{Please try again.}")
                
                tree_msg = "Tree could not be generated for invalid input."

            else:
                T = "\\textbf{{Analysis of }} {}".format(soln[0])
                ans.append("c_{crit} = \\textit{the work to split/recombine vs subproblems}")
                ans.append("= \\textit{log(# of subproblems)/log(relative problem size)}")
                ans.append("= log(a)/log(b)")
                ans.append(soln[1])
                ans.append("= {}".format(soln[2]))
                ans.append("\\text{{From this we deduce }} {} \\text{{, which then implies we have case }} {}".format(soln[3], soln[4]))
                ans.append("\\therefore {}".format(soln[5]))
                tree_msg = "As seen below, the recursion tree is {} in this case.".format(soln[6])                

            args = {'form': form, 'T': T, 'ans': ans, 'tree_msg': tree_msg, 'nodes2': nodes2, 'nodes3': nodes3, 'leaves': leaves, 'height': height, 'a': a, 'b': b, 'k': k, 'i': i}

            # init blank form
            form = MastersForm()

        return render(request, self.template_name, args)
