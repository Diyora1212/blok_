from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views import View
from .models import Post
from .forms import UserRegisterModelForm, PostCreateForm, UserLoginForm, PostUpdateForm, PostDeleteForm


class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'blog/about.html')


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form = PostCreateForm
    fields = ['title', 'content', 'author', 'date_posted']
    success_url = reverse_lazy('Diyora:user')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostsView(ListView):
    form = PostUpdateForm, PostDeleteForm
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'



class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('Diyora:user')
    success_message = 'Post was deleted successfully'


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterModelForm()
        return render(request, "blog/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User successfully registered")
            form.save()
            return redirect("Diyora:login-page")
        else:
            return render(request, "blog/register.html", {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "blog/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "user successfully logged in")
                return redirect("Diyora:home-page")
            else:
                messages.error(request, "Username or password wrong")
                return redirect("Diyora:login-page")

        else:
            return render(request, "blog/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        return render(request, "blog/logout.html")

    def post(self, request):
        logout(request)
        messages.info(request, "User successfully loged out")
        return redirect("Diyora:home-page")
