from django.urls import path
from . import views  # . means root

urlpatterns = [
    path('', views.index, name="list"),  # home-page
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
