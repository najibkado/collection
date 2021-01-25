from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('api/login', views.LoginApiView.as_view()),
    path('api/register', views.UserRegisterApiView.as_view()),
    path('api/entry', views.EntriesApiView.as_view()),
    path('api/entry/<int:id>', views.EntryApiView.as_view())
]