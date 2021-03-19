from django import forms
from .import models
from .models import SubjectList,Studylist

class SelectSubject(forms.ModelForm):
    class Meta:
        model=Studylist
        fields=[
            "subjectlist"
        ]