"""todoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = "main"  
 
urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('takeNote', views.takeNote, name="takeNote"), 
    path('deleteNote', views.deleteNote, name="deleteNote"), 
    path('achieved', views.achieved, name="achieved"), 
    # path('tinymce', include('tinymce.urls')),
]
