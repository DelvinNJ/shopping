from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('grapes',views.grapes,name='grapes'),
    path('register/',views.Register,name='register'),
    path('logout/',views.Logout,name='logout'),
]