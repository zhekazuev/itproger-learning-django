from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView

def news_home(request):
    news = Article.objects.order_by("-date")
    return render(request, "news/news_home.html", {"news": news})

class NewsDetailView(DetailView):
    model = Article
    template_name = "news/details_view.html"
    context_object_name = 'article'

def create(request):
    error = None
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "Form is invalid"

    form = ArticleForm()
    data = {
        "form": form,
        "error": error
    }
    return render(request, "news/create.html", data)
