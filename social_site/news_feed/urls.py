from django.urls import path
from .views import NewsDetailView, NewsFeedView

urlpatterns = [
    path('', NewsFeedView.as_view(), name='news-feed'),
     path('<int:news_id>/', NewsDetailView.as_view(), name='news-detail'),
]
