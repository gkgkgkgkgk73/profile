from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('multi/', views.multi, name='multi'),
    path('career/', views.career, name='career'),
]