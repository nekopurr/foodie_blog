from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Comment
from .forms import CommentForm, PostForm

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
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm()
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form
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
        context = {
            'form': form
        }
        return render(request, 'blog/post_write.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            post = form.save(commit=False) # 저장을 잠시 보류하고,
            post.writer = request.user # 현재 로그인한 사용자를 작성자로 설정
            post.save() # 저장
            return redirect('blog:post_detail', pk=post.pk)
        return render(request, 'blog/post_write.html', context)


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