from django.views.generic import ListView
import pdb
from django.shortcuts import render

from news.models import Post


class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(categore__slug=self.kwargs.get("slug"))

def home(request):
    return render(request, 'base.html')
