"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from calc import views as calc_views
from learn import views as learn_views
from tools import views as tools_views

urlpatterns = [
    path('tools', tools_views.index, name='tools'),
    path('', calc_views.index, name='home'),
    # path('', learn_views.index, name='home'),
    path('polls/', include('polls.urls')),
    # name 可以用于在 templates, models, views ……中得到对应的网址，相当于“给网址取了个名字”，只要这个名字不变，网址变了也能通过名字获取到。
    path('add/', calc_views.add, name='add'),
    path('add/<int:a>/<int:b>', calc_views.add2, name='add2'),
    path('admin/', admin.site.urls),
]
