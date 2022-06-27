from django.views import generic
from .models import Post
from django.urls import reverse_lazy
    
class PostCreateView(generic.CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
    

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
    template_name = 'post_confirm_delete.html'
