from django.urls import path
from .import views

app_name='studylist'
urlpatterns=[
    path('',views.Study.as_view(),name='studylist'),
    ]
