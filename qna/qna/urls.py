"""
URL configuration for qna project.

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
from django.urls import path
from home.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home,name = 'home'),
    path('signup/',signup_view,name = 'signup'),
    path('login/', login, name = "login"),
    path('logout/', logout, name = 'logout'),
    path('ask/', ask_view, name = 'ask_view'),
    path('answer/<int:id>/',show_answer_view,name = 'answer'),
    path('profile/',profile_view,name = 'profile'),
    path("verify/",verify,name="verify"),
    path('recover/',recover, name= "recover"),
    path('category/<str:cat>',category_view,name = 'category'),
    path("search/", search,name="search"),
]
