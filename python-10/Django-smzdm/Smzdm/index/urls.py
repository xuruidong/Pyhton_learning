"""Smzdm URL Configuration

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
from django.urls import path
from django.urls import re_path
from django.urls import register_converter

from . import views

class IntConverter():
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

register_converter(IntConverter, 'myint') 

urlpatterns = [
    path('', views.index),
    path('<int:year>', views.myyear, name='myyear'),
    path('<int:year>/<str:name>', views.abc),
    # re_path('(?P<year>[0-9]{3})', views.re_year)
    path('<myint:mm>', views.mmm),
    path('comment', views.comment)
]
