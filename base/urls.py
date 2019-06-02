from django.urls import path 
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view()), # new
    path('users/<int:pk>/', views.UserDetail.as_view()), # new
]
urlpatterns = format_suffix_patterns(urlpatterns)
