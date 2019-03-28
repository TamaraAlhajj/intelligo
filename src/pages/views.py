from django.shortcuts import render
from django.views.generic import TemplateView
from pages.forms import ComplexityForm


class Home(TemplateView):
    template_name = "home.html"


class Info(TemplateView):
    template_name = "info.html"


class BigO(TemplateView):
    template_name = "bigO.html"

    def get(self, request):
        form = ComplexityForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ComplexityForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            # init blank form
            form = ComplexityForm()

        args = {'form': form, 'text': text}
        
        return render(request, self.template_name, args)


class Masters(TemplateView):
    template_name = "masters.html"
