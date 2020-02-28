from django.urls import path
from . import views
from .views import home, add_todo, delete_todo
urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:pk>/', views.delete_todo)
]