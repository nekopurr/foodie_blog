from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        # writer 필드는 모델에서 ForeignKey로 설정되어있어서 직접 받을 필요가 없음


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
            )