from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인 되었습니다.')
            return redirect('blog:post_list')
        else:
            messages.error(request, '로그인에 실패하였습니다.')
    return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('blog:post_list')