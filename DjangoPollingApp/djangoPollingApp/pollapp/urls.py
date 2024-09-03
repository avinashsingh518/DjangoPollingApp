from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('admin', admin.site.urls),
    path('wel/', views.wel, name='wel'),
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('wel/delete/', views.delete, name='delete'),
    path('register/',RegisterAPI.as_view() ),
    path('index/', views.index, name = 'index'),
    path('vote/<str:pk>', views.vote, name = 'vote'),
    path('result/<str:pk>', views.result, name = 'result'),
    path('logout/',views.logout,name='logout'),

]