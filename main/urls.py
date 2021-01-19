from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/entry', views.EntriesApiView.as_view()),
    path('api/entry/<int:id>', views.EntryApiView.as_view())
]