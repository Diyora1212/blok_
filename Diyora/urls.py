from django.urls import path
from .views import home_view, about_view, login_view, post_detail_view, post_form_view, post_confirm_delete_view, register_view, user_posts_view

app_name = 'Diyora'
urlpatterns = [
    path('', home_view, name='home-page'),
    path('about/', about_view, name='about-page'),
    path('login/', login_view, name='login-page'),
    path('posts/', post_detail_view, name='post-detail-page'),
    path('posts/<int:pk>/', post_form_view, name='post-form-page'),
    path('posts/confirm/delete/', post_confirm_delete_view, name='post-confirm'),
    path('register/', register_view, name='register-page'),
    path('user_posts/', user_posts_view, name='user'),
]