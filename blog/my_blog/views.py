from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'my_blog/home.html', context)

def about(request):
    return render(request, 'my_blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'my_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'my_blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdate(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
        model = Post
        fields = ['title', 'content']

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
        

        def test_func(self):
             post = self.get_object()
             if self.request.user == post.author:
                  return True
             return False
             
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
             post = self.get_object()
             if self.request.user == post.author:
                  return True
             return False