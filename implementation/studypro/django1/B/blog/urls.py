from django.urls import path
from . import views

urlpatterns =[
    path('', views.show_blog, name='show_blog'),
    path('<int:blog_id>/', views.detail_blog, name='detail_blog'),
    path('tag/<slug:tag>', views.filter_tag, name='filter_tag'),
    path('cat/<slug:category>', views.filter_category, name='filter_category'),
    path('search/<str:field>', views.search, name='search'),
    path('add_blog/', views.add_blog, name='add_blog'),
]