from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'main/index.html'

# def home(request):
#     return render(request, "main/index.html")
