from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

class BrowseView(TemplateView):
    template_name = 'index.html'
