from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView # new
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'



#  By default, DetailView will provide a context object we can use in our
# template called either object or the lowercased name of our model, which would be post.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    #. For fields we explicitly set the database fields we want to expose which are title, author, and body.
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): # new 
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']