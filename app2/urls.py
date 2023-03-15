from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('Sample3/',Sample3,name='Sample3'),
    path('Sample4/',Sample4,name='Sample4'),
    
]