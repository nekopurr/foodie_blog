from django.shortcuts import render

def Index(request):
    context = {
        'title': '메인 페이지',
    }
    return render(request, 'index.html', context)
