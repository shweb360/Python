from django.conf.urls import url
from django.urls import path,include
from . import views,testdb,search,search_post

urlpatterns = [
   url(r'^$', views.index),
   path('about/',views.about),
   path('hello/', views.hello),  

   #数据库操作 
   path('add/', testdb.add),
   path('query/', testdb.query),
   path('update/', testdb.update),
   path('delete/', testdb.delete),

   #表单
   path('search_form/',search.search_form),
   path('search/', search.search),
   path('search_post/', search_post.search_post),
   
]