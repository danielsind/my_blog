from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreate, PostUpdate, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name = 'post-update'),
    path('post/new', PostCreate.as_view(), name = 'post-create'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),
]