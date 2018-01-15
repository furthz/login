from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'

class CCMCognitivo(generic.TemplateView):
    template_name = 'ccm_cognitivo.html'



