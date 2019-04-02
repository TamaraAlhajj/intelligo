from django.shortcuts import render
from django.views.generic import TemplateView
from pages.forms import ComplexityForm, MastersForm
from pages.models import ComplexityPost, MastersPost
from django.shortcuts import render, redirect
from pages.MathsLogic import bigO, masters


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
            f = soln[0]
            g = soln[1]
            const = soln[2]

            # init blank form
            form = ComplexityForm()

        args = {'form': form, 'f': f, 'g': g, 'const': const}
        return render(request, self.template_name, args)


class Masters(TemplateView):
    template_name = "masters.html"

    def get(self, request):
        form = MastersForm()
        #post = ComplexityPost.objects.all().order_by('-date')[0]

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = MastersForm(request.POST)
        if form.is_valid():
            form.save()
            a = int(form.cleaned_data['post_a'])
            b = int(form.cleaned_data['post_b'])
            k = int(form.cleaned_data['post_k'])
            i = int(form.cleaned_data['post_i'])

            soln = masters(a, b, k, i)
            ans = list()

            if (type(soln) == str):
                T = "\\textbf{Invalid Input}"

                ans.append("\\text{{{}}}".format(soln))
                ans.append("\\text{Please try again.}")
                
                args = {'form': form, 'T': T, 'ans': ans}

            else:
                T = soln[0]

                ans.append("c_{crit} = \\textit{the work to split/recombine vs subproblems}")
                ans.append("= \\textit{log(# of subproblems)/log(relative problem size)}")
                ans.append("= log(a)/log(b)")
                ans.append(soln[1])
                ans.append("\\approx {}".format(soln[2]))
                ans.append("\\text{{From this we deduce }} {} \\text{{, which then implies we have case }} {}".format(soln[3], soln[4]))
                ans.append("\\therefore {}".format(soln[5]))
                tree_msg = "As seen below, the recursion tree is {} in this case.".format(soln[6])

                args = {'form': form, 'T': T, 'ans': ans, 'tree_msg': tree_msg}

            # init blank form
            form = MastersForm()

        return render(request, self.template_name, args)
