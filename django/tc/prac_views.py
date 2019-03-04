from django.shortcuts import render, redirect #장고 임포트
from .models import Post #모델즈의 class이름을 임포트함

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.htm', {'posts':posts})

def detail(request, url에서입력받는_id):
    post = Post.objects.get(pk=url에서입력받는_id) #pk프라이머리키로 파이썬에서 정보를 얻음
    return render(request, 'detail.htm', {'post':post})

# def delete(request, url에서입력받는_id):
#     if request.method == 'POST':
#         post = Post.objects.get(pk=url에서입력받는_id)
#         post.delete()
#         return redirect('posts:list')
#     else:
#         return render(request,'delete.htm')

def delete2(request, url에서입력받는_id):
    post = Post.objects.get(pk=url에서입력받는_id)
    post.delete()
    return redirect('/posts/')