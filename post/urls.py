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
   path('Added_post',views.Added_post,name='Added_post'),
   path('delete/<int:id>',views.post_delete,name='delete'),
   path('pass_comment',views.pass_comment,name='pass_comment'),
   path('to_save_comment',views.to_save_comment,name='to_save_comment')

]

