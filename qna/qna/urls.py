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
from django.conf import settings #add this
from django.conf.urls.static import static #add this
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name = "home"),
    path('about/',about,name = "about"),
    path('answer/<int:id>/',show_answer_view,name = 'answer'),
    path('profile/user/<str:u>/', profile_view_other,name="profile view other"),
    path('profile/user/<str:u>/answer/', profile_view_other_answer,name="profile view other answer"),
    # path('search/',search_view,name = 'search'),
    path('signup/',signup_view,name = 'signup'),
    path('login/', login, name = "login"),
    path('recover/',recover, name= "recover"),
    path('ask_question/',ask_question_view,name = 'askquestion'),
    path('pagination/',pagination_view,name = 'pagination'),
    path('profile/',profile_view,name = 'profile'),
    path('profile_setting/',profile_setting_view,name = 'profilesetting'),
    path('category/<str:cat>',category_view,name = 'category'),
    path('logout/', logout, name = 'logout'),
    path('profile/answer/', profile_view_answer, name="profile_view"),
    path('profileedit/', profileedit,name ="Profile edit"),
    path("upload", upload, name="upload"),
    path("search/", search,name="search"),
    path("verify/",verify,name="verify"),
    path('changed/',pass_changed,name = "password changed"),
    path('message/<int:recv_id>',message,name = "messaging"),
    path('message/send/<int:recv_id>',send_message,name = "send messaging"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
