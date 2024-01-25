from django.urls import path
from . import views


urlpatterns = [
   path('completed/', views.surveycomp, name='surveycomp'),
   
]
