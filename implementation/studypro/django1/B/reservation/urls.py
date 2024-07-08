from django.urls import path
from . import views

urlpatterns =[
    path('', views.reserve, name='book'),
    path('update/<int:user_id>/<int:tb_id>/', views.update_table, name='updatetable'),
]