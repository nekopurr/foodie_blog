from django.urls import path
from .views import PostListView, PostDetailView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", PostListView.as_view(), name='list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/comment', CommentCreateView.as_view(), name='comment_create'),
]