from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogs'),
    path('blogpost/<int:pk>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    #path('bloggers/', views.BloggerListView.as_view(), name=blogger-list'),

    
]