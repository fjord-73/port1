from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name='sample'),
    path('fb', views.form, name='form'),
    path('fb_order', views.post_ok, name='post_ok'),
    path('path', views.creates, name='creates'),
    path('database', views.database, name='database'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('login_ok', views.login_ok, name='login_ok'),
    path('link', views.link, name='link'),
    path('intro', views.introduction, name='introduction'),
    path('merit', views.merit, name='merit'),
]