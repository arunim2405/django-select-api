"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.LoanModelView)
urlpatterns = [
	path('form/', views.cxcontact, name='myform'),
    path('api/', include(router.urls)),
    #path('status/', views.loanmodelreject),
    path('newform/', views.cxcontact2, name='mynewform'),
    #main api call is status2 for selected queries and api/MyAPI for all queries
    path('status2/', views.returnobj),
] 