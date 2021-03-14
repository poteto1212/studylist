from django.contrib import admin
from study.models import SubjectList,Studylist

adminlists=[SubjectList,Studylist]

for adminlist in adminlists:
    admin.site.register(adminlist)
