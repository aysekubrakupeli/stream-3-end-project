from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import BlogPostForm, BlogCommentForm
from django.utils import timezone

# Create your views here.

def blogposts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render (request, "blogposts.html", {"posts": posts})

def viewpost(request, id):
    post = get_object_or_404(Post, pk=id)
    post_id = post.pk
    comments = Comment.objects.filter(post=post)
    form = BlogCommentForm()
    liked = False
    if request.session.get('has_liked_'+str(post_id), liked):
        liked = True
        print("liked {}_{}".format(liked, post_id))
    return render(request, "viewpost.html", {'post': post, 'comments': comments, 'form': form, 'liked': liked})

@login_required()
def newpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            request.user.profile.ego += 10
            request.user.profile.save()
            post.save()
            return redirect(viewpost, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'newpost.html', {'form': form})
    
def editpost(request, id):
   post = get_object_or_404(Post, pk=id)
   if request.method == "POST":
       form = BlogPostForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.created_date = timezone.now()
           post.save()
           return redirect(viewpost, post.pk)
   else:
       form = BlogPostForm(instance=post)
   return render(request, 'newpost.html', {'form': form})
   
def addcomment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = BlogCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        request.user.profile.ego += 3
        request.user.profile.save()
        comment.save()
        return redirect('viewpost', post_id)