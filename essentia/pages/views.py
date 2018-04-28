from django.shortcuts import render, redirect
from .forms import CareersForm
from django.views.generic import TemplateView


class CareersPage(TemplateView):
    template_name = 'pages/careers.html'

    def get(self, request):
        form = CareersForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CareersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('careers')
