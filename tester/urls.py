
from unicodedata import name
from django.urls import path,include
from .views import render_pdf_view1, render_view_download1, pdflist, profile_name1,profile_name2, render_pdf_view2, render_view_download2
from . import views
app_name = 'profile'
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('pdflist',pdflist ,name='pdflist'),
    #first template
    path('template1/',profile_name1.as_view(),name='profile_name1'),
    path('template1/show/<pk>',render_pdf_view1,name='render_pdf_view1'),
    path('template1/pdf/<pk>',render_view_download1,name='render_view_download1'),
    #second template
    path('template2/',profile_name2.as_view(),name='profile_name2'),
    path('template2/show/<pk>',render_pdf_view2,name='render_pdf_view2'),
    path('template2/pdf/<pk>',render_view_download2,name='render_view_download2')
    
]
