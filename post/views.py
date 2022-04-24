from django.shortcuts import render
from .models import Post 
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, "post/home.html", context)

def about(request):
    return render(request, 'post/about.html')

def contact(request):
    return render(request, 'post/contact.html')