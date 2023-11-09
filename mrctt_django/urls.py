"""
URL configuration for mrctt_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from ppage import views as v_ppage
# from projects import views as v_projects

urlpatterns = [
    #path('admin/', admin.site.urls, name='admin_home'),

    path('admin/', admin.site.urls),

    path('', include('ppage.urls')),

    path('projects/', include('projects.urls')),

    path('qrgen/', include('qrgen.urls')),

    # path('home/',v_ppage.ppage),
    # stessa cosa di #path('', include('ppage.urls')), 
    # ma senza dover dichiarare nulla nel file urls.py dell'app ppage

    # path('', v_ppage.wpage),

    # path('projects/', v_projects.projects)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
