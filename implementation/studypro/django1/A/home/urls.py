from django.urls import path
from . import views
#. means from this directory

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.say_hello),
    path('detail/<int:todo_id>/', views.details, name= 'details'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('create/',views.create, name='create'),
]