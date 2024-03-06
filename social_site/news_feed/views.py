from django.shortcuts import render, redirect
from django.views import View
from .models import News
from .forms import CommentForm, NewsForm

class NewsFeedView(View):
    template_name = 'news_feed/news_feed.html'

    def get(self, request):
        news_feed = News.objects.all().order_by('-created_at')
        form = NewsForm()
        return render(request, self.template_name, {'news_feed': news_feed, 'form': form})

    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
        return redirect('news-feed')

class NewsDetailView(View):
    template_name = 'news_feed/news_detail.html'

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        comments = news.comments.all()
        form = CommentForm()
        return render(request, self.template_name, {'news': news, 'comments': comments, 'form': form})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.author = request.user
            comment.save()
            return redirect('news-detail', news_id=news_id)

        comments = news.comments.all()
        return render(request, self.template_name, {'news': news, 'comments': comments, 'form': form})