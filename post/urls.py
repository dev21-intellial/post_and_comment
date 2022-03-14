from django.contrib import admin
from post import views
from django.urls import path,include

urlpatterns = [
   path('registration',views.registration,name='registration'),
   path('',views.login,name='login'),
   path('authenticate',views.authenticate_user,name='authenticate'),
   path('add_user',views.add_user,name='add_user'),
   path('show',views.show,name='show'),
   path('compose',views.compose,name='compose'),
   path('post',views.post,name='post'),
   path('delete/<int:id>',views.post_delete,name='delete'),
   path('pass_comment/<int:id>',views.pass_comment,name='pass_comment'),
   path('given_comment/<int:id>',views.given_comment,name='to_save_comment'),
   path('likes/<int:id>',views.likes,name='likes'),
   path('dislike/<int:id>',views.dislike,name='dislike'),
   path('add_post',views.add_post,name="add_post"),
   path('delete_comment/<int:id>',views.delete_comment,name='delete_comment'),

]

