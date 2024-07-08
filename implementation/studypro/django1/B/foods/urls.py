from django.urls import path
from . import views

#app_name = 'foods'

urlpatterns =[
    path('', views.show_food, name='show'),
    path('<int:food_id>/detail/', views.detail_food, name='detail'),
    path('sabad/', views.final_sabad, name='sabad'),
    path('<int:user_id>/pay/', views.pay, name='pay'),
    path('<int:user_id>/carthistory/', views.cart_history, name='history'),
    path('<int:user_id>/wallet/', views.charge_wallet, name='wallet'),
    path('<int:user_id>/<str:order_number>/cancle/', views.cancle_order, name='cancle'),
    path('<int:user_id>/show_vote/', views.show_vote, name='show_vote'),
    path('<int:user_id>/<int:food_id>/vote/', views.vote, name='vote'),
]