from django.urls import path
from . import views
from . views import RankList, RankDetail
urlpatterns = [
    
   path('', views.index, name='index'),
   path('create', views.create, name='create'),
   path('edit/<int:num>', views.edit, name='edit'),
   path('delete/<int:num>', views.delete, name="delete"),
   path('list', RankList.as_view()),
   path('detail/<int:pk>', RankDetail.as_view()),
   path('find', views.find, name='find'),
   path('check', views.check, name='check'),
   path('<int:num>', views.index, name='index'),
   path('message/', views.message, name='message'),
   path('message/<int:page>', views.message, name='message'),
]    