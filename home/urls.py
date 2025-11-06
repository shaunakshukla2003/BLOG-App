from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('blog/<slug:slug>/',views.blog,name='blog'),
    path('newblog/',views.newblog,name='newblog'),
    path('editblog/<str:slug>/',views.editblog,name='editblog'),
    path('deleteblog/<str:slug>/',views.deleteblog,name='deleteblog'),   
]
