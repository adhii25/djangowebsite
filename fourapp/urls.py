from.import views
from django.urls import path

urlpatterns=[
    path('',views.demo,name='demo'),
    path('', views.pics, name='pics'),

    #    path('div/',views.division,name='division'),
]