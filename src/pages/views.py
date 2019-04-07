from django.shortcuts import render
from django.views.generic import TemplateView
from pages.forms import ComplexityForm, MastersForm
from pages.models import ComplexityPost, MastersPost
from django.shortcuts import render, redirect
from pages.logicLayer import bigO, masters, generate_tree


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

            if(type(soln) == str):
                f = soln
                g = "\\text{Make sure you are using python syntax for math expressions.}"
                lim = ["Please try again."]
            else:
                f = "$$\\text{{Analysis of }} f(n) = {}$$".format(soln[0])
                g = "f(n) = O({}) ".format(soln[1])
                const = soln[2]
                omega = soln[3]
                
                lim.append("Using limits we can deduce the bounds, and thus the run-time, of the function.")
                lim.append("$$ \lim_{{n \\to +\infty}} \\frac{{{}}}{{{}}} = {}$$".format(soln[0], soln[1], const))
                lim.append("Thus, this function has a upper bound of, $${}$$.".format(g))
                lim.append("This is the worst case run-time.")
                
                if(const is not 0):
                    more.append("Since the limit as n grows to infinity is greater than 0 we can also say,")
                    if(soln[4]):
                        more.append("$${} \\textbf{{ and }} f(n) = \\Omega({}) \\implies \\Theta({})$$".format(g, omega, omega))
                        more.append("Thus we can say f(n) is tight bound by g(n), meaning the functions grow at approximately the same rate.")
                    else:
                        more.append("$${} \\textbf{{ and }} f(n) = \\Omega({})$$".format(g, omega))
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
            try:
                a = int(form.cleaned_data['post_a'])
                b = int(form.cleaned_data['post_b'])
                k = int(form.cleaned_data['post_k'])
                i = int(form.cleaned_data['post_i'])

                 # run maths
                soln = masters(a, b, k, i)
                ans = list()

                # create tree and function will return respective height
                height = generate_tree(a, b, k, i)

                if (type(soln) == str):
                    T = "\\textbf{Invalid Input}"

                    ans.append("\\text{{{}}}".format(soln))
                    ans.append("\\text{Please try again.}")
                    tree_msg = "\\text{This is an example tree which shows the first 3 levels of the recursion tree for } a=2." 
                    height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(height)           

                else:
                    T = "\\textbf{{Analysis of the recurrence }} {}".format(soln[0])
                    ans.append(soln[1])
                    ans.append("\\text{{From this we deduce }} {} \\text{{, which then implies we have case }} {}".format(soln[2], soln[3]))
                    ans.append("\\textbf{{ \\therefore the solution is }} {}".format(soln[4]))
                    tree_msg = "\\text{This is the first 3 levels of the recursion tree for } f(n)." 
                    height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(height)   

                args = {'form': form, 'T': T, 'ans': ans, 'tree_msg': tree_msg, 'height': height, 'a': a, 'b': b, 'k': k, 'i': i}        
            
            except:
                
                T = "\\textbf{Invalid Input}"
                ans = ["\\text{Please try again.}"]
                tree_msg = "\\text{This is an } \\textbf{example } \\text{tree which shows the first 3 levels of the recursion tree for } a=2."
                height = generate_tree(2, 1, 1, 1) ## trigger example from bad input for tree gen
                height = "\\text{{These branches will continue to split until the tree is a height of }} {}.".format(height)           

                args = {'form': form, 'T': T, 'ans': ans, 'tree_msg': tree_msg, 'height': height}        

            # init blank form
            form = MastersForm()

        return render(request, self.template_name, args)
