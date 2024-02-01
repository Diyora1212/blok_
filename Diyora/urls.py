from django.urls import path
from .views import  HomeView, AboutView, PostCreateView, UserPostsView, PostDetailView, PostDeleteView, UserRegisterView, UserLoginView, UserLogoutView
app_name = 'Diyora'
urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('about/', AboutView.as_view(), name='about-page'),
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail-page'),
    path('posts/new/', PostCreateView.as_view(), name='post-form-page'),
    path('posts/<int:pk>/confirm/delete/', PostDeleteView.as_view(), name='post-confirm'),
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('posts/', UserPostsView.as_view(), name='user'),
    path('logout/', UserLogoutView.as_view(), name='logout-page')
]