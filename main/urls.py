from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('dashboard', views.dashboard_view, name="dashboard"),
    path('dashboard/folder/<int:id>', views.dashboard_folder_view, name="dashboard-folder"),
    path('dashboard/file/<int:id>', views.dashboard_file_view, name="dashboard-file"),
    path('api/logout', views.LogoutApiView.as_view()),
    path('api/login', views.LoginApiView.as_view()),
    path('api/register', views.UserRegisterApiView.as_view()),
    path('api/entry', views.EntriesApiView.as_view()),
    path('api/entry/<int:id>', views.EntryApiView.as_view())
]