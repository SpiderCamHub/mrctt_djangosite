from django.urls import path
from ppage import views

urlpatterns = [
    path('', views.ppage, name='ppage_home'),
]
