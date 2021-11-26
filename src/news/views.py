from django.shortcuts import render
from .models import Article

def news_home(request):
    news = Article.objects.order_by("date")
    return render(request, "news/news_home.html", {"news": news})
