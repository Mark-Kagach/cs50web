from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("profile/<str:account>/", views.profile, name="profile"),
    path("following", views.following, name="following"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("like/<int:post_id>", views.like, name="like")
]
