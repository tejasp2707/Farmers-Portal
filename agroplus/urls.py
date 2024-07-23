from django.contrib import admin
from django.urls import path
from agroplus import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('farmercorner', views.farmercorner, name='farmercorner'),
    path('Buy', views.Buy, name='Buy'),
    path('Sell', views.SellFun, name='Sell'),
    path('Croprate', views.Croprate, name='Croprate'),
    path("login",views.loginpage,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("register",views.registerpage,name="register"),
    path("feedback",views.feedback,name="feedback"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 