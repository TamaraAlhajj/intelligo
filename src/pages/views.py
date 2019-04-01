from django.shortcuts import render
from django.views.generic import TemplateView
from pages.forms import ComplexityForm
from pages.models import ComplexityPost
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
            form.save()
            text = form.cleaned_data['post']

            soln = bigO(text)
            f = soln[0]
            g = soln[1]
            const = soln[2]

            # init blank form
            form = ComplexityForm()
            #return redirect('bigO')

        args = {'form': form, 'fn': f, 'g': g, 'const': const}
        return render(request, self.template_name, args)


class Masters(TemplateView):
    template_name = "masters.html"
