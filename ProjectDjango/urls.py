"""ProjectDjango URL Configuration

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
from django.contrib import admin
from django.urls import path
from AppFirst.views import home, lista, nova_transacao, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_login'),
    path('read/', lista, name='url_lista'),
    path('create/', nova_transacao, name='url_nova'),
    path('update/<int:pk>', update, name='url_update'),
    path('delete/<int:pk>', delete, name='url_delete')
]