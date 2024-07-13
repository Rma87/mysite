from django.shortcuts import render
from blog.models import Post
def blog(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blog template/blog-home.html',context)

def blog_single(request):
    return render(request, 'blog template/blog-single.html')