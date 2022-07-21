from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView, DetailView


# Create your views here.
class BlogListView(ListView):
    
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'all_posts_list'


class BlogDetailView(DetailView):
    
    model = Post
    template_name = 'blogapp/post_detail.html'


class About(TemplateView):
    
    model = Post
    template_name = 'blogapp/about.html'
