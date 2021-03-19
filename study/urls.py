from django.urls import path
from .import views

app_name='studylist'
urlpatterns=[
    path('',views.Study.as_view(),name='studylist'),
    path('problemlist/',views.StudylistView.as_view(),name='problemlist'),
    path('problemlist/',views.Select.as_view(),name='problemlist')
    ]
