from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm

# Create your views here.

### Post
class PostListView(View):

    def get(self, request):
        posts = Post.objects.all()
        category_list = Category.objects.all()
        context = {
            "posts": posts,
            "category_list": category_list,
            "title": '게시판',
        }
        return render(request, 'blog/post_list.html', context)


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm()
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'title': post.title,
            'categories': Category.objects.all(),
        }
        return render(request, 'blog/post_detail.html', context)


class PostEditView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=pk)
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)


class PostWriteView(View):
    def get(self, request):
        form = PostForm()
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'blog/post_write.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
        }
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
        return render(request, 'blog/post_write.html', context)


class PostDeleteView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blog:list')


class CommentWriteView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('blog:post_detail', pk=post.pk)