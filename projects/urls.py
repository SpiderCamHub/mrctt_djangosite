from django.urls import path
from projects import views

urlpatterns = [
    path('', views.project_home, name='projects_home'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
