from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

### Post
class PostListView(View):

    def get(self, request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
            # "title": "Blog",
        }
        return render(request, 'blog/post_list.html', context)


class PostDetailView(View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form
            }
            comments = Comment.objects.filter(post=post)
            comment_form = CommentForm()
            return render(request, 'blog/post_detail.html', context)
        except Post.DoesNotExist:
            return redirect('blog:post_list')


class CommentCreateView(View):
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
            return redirect('blog:post_detail', pk=post.pk)
        except Post.DoesNotExist:
            return redirect('blog:post_list')