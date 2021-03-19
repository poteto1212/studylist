from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import FormView
from .import forms
from .models import Studylist,SubSubjectList,SubjectList
from .forms import SelectSubject

class Study(generic.TemplateView):
    template_name='study/study.html'
     
     
class StudylistView(generic.ListView):
    template_name='study/problemlist.html'
    model=Studylist

class Select(FormView):
    form_class=forms.SelectSubject
    template_name='study/problemlist.html'

  