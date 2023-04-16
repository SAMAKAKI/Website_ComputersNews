from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="news"),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.NewsDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.NewsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.NewsDeleteView.as_view(), name='delete'),
]