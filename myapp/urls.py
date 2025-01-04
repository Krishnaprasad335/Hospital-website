
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('doctor/',views.doctor,name='doctor'),
    path('department/',views.department,name='department'),
    path('booking/',views.booking,name='booking')
]