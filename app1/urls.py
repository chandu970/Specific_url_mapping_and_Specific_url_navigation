from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('Sample1/',Sample1,name='Sample1'),
    path('Sample2/',Sample2,name='Sample2'),
]