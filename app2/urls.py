from app2.views import *
from django.urls import path
app_name='Nothing'
urlpatterns=[
    path('response/',response,name='response')
]