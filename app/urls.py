
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
   ################################Home page###########
   path('' , home , name='home' ), 
   ################################login page###########
   path('login/' ,login  , name='login'), 
   ################################sign up page###########
   path('signup/' , signup ), 
   ################################add to do task page###########
   path('add-todo/' , add_todo ), 
   ################################delete to do task page###########
   path('delete-todo/<int:id>' , delete_todo ), 
   ################################change to do task page###########
   path('change-status/<int:id>/<str:jarayon>' , change_todo ),
   ################################log out user page########### 
   path('logout/' , signout ), 
]
