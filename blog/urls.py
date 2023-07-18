from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", views.PostListView.as_view(), name='list'),
    
]