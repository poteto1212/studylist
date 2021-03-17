from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Studylist
from .models import SubSubjectList

class Study(generic.TemplateView):
    template_name='study/study.html'
     
     
class StudylistView(generic.ListView):
    template_name='study/problemlist.html'
    model=Studylist
    