from django.urls import path
from . import views

urlpatterns=[
    path('',views.allblog, name='blog'),
    path('blog-form',views.userblogform, name='blog-form'),
    path('updateblog-form/<str:pk>/',views.userblogformupdate, name='blogupdate'),
    path('addauthor/',views.addauthorform,name='addauthor'),
    path('delblog/<str:pk>',views.deleteblog, name='deleteblog')
]