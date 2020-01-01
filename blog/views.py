from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def blogHome(request):
	blogs = Blog.objects
	return render(request, "blog/home.html", {"bl" : blogs})

def details(request,blog_id):
	detailBlog = get_object_or_404(Blog,pk = blog_id)
	return render(request, 'blog/details.html', {'details' : detailBlog})
