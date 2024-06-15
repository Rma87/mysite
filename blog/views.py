from django.shortcuts import render

def blog(request):
    return render(request, 'blog template/blog-home.html')

def blog_single(request):
    return render(request, 'blog template/blog-single.html')