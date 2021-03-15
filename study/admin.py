from django.contrib import admin
from study.models import SubjectList,SubSubjectList,Studylist

adminlists=[SubjectList,SubSubjectList,Studylist]

for adminlist in adminlists:
    admin.site.register(adminlist)
