from django.conf.urls import url
from django.urls import path,include
from . import views,testdb

urlpatterns = [
   url(r'^$', views.index),
   path('about/',views.about),
   path('hello/', views.hello),   
   path('add/', testdb.add),
   path('query/', testdb.query),
   path('update/', testdb.update),
   path('delete/', testdb.delete),
]