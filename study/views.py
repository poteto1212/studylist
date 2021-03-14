from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

class Study(generic.TemplateView):
    template_name='study/study.html'
     
     
         

