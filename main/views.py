from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post_list_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        is_active = request.POST.get('is_active') == 'on'
        
        Post.objects.create(
            title=title,
            desc=desc,
            image=image,
            is_active=is_active
        )
        return redirect('/')
    
    return render(request, 'post_form.html')

def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.desc = request.POST.get('desc')
        post.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        
        post.save()
        return redirect('/')
    
    return render(request, 'post_form.html', {'post': post})

def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    
    return render(request, 'post_confirm_delete.html', {'post': post})