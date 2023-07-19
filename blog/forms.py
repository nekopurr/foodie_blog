from django import forms
from .models import Comment, Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        # writer 필드는 모델에서 ForeignKey로 설정되어 있어서 폼에 직접 받을 필요가 없음



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
            )