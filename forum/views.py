from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'forum/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/forum/')

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