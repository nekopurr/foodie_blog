from django.urls import path
from .views import PostListView

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", PostListView.as_view(), name='list'),
    
]