from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'forum/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')


#     return render(
#         request,
#         'forum/index.html',
#         {
#             'posts': posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'forum/single_post_page.html',
#         {
#             'post': post,
#         }
#     )