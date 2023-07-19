from django.urls import path
from .views import PostListView, PostWriteView, PostDetailView, PostEditView, PostDeleteView, CommentWriteView

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", PostListView.as_view(), name='list'),
    path('write/', PostWriteView.as_view(), name='post_write'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/comment', CommentWriteView.as_view(), name='comment_create'),
    path('<int:pk>/edit', PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]