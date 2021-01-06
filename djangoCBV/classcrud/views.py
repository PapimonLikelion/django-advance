from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

# Create your views here.

#제네릭 뷰에서는 render 할 html 파일의 이름을 모델(소문자로 변경)_list/form/detail/confirm_delete.html를 default로 가짐

class BlogView(ListView):
    model = ClassBlog

class BlogCreate(CreateView):
    model = ClassBlog
    fields = ['title', 'body'] # 모델 form 중 내가 입력할게 
    success_url = reverse_lazy('list') # 블로그 객체가 성공적으로 생성시 success_url로 redirect 해주세요 

class BlogDetail(DetailView):
    model = ClassBlog

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')