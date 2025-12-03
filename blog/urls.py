from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogs'),
    path('blogpost/<int:pk>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('bloggers/', views.BloggersListView.as_view(), name='blogger-list'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogpost/<int:pk>/comment/', views.add_comment, name='add-comment'),

]