from django.urls import path
from qrgen import views

urlpatterns = [
    path('', views.qrgen_home, name='qrgen_home'),
    path('result/', views.qrgen_result, name='qrgen_result'),
]
