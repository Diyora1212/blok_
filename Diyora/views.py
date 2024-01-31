from django.shortcuts import render

from django.http import HttpResponse


def home_view(request):
    return render(request, 'blog/home.html')


def about_view(request):
    return render(request, 'blog/about.html')


def login_view(request):
    return render(request, 'blog/login.html')


def post_detail_view(request):
    return render(request, 'blog/post_detail.html')


def post_form_view(request):
    return render(request, 'blog/post_form.html')


def post_confirm_delete_view(request):
    return render(request, 'blog/post_confirm_delete.html')


def register_view(request):
    return render(request, 'blog/register.html')


def user_posts_view(request):
    return render(request, 'blog/user_posts.html')

# Create your views here.
