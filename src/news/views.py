from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Article.objects.order_by("-date")
    return render(request, "news/news_home.html", {"news": news})

class NewsDetailView(DetailView):
    model = Article
    template_name = "news/details_view.html"
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Article
    template_name = "news/create.html"
    # fields = ["title", "anons", "full_text", "date"]
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    template_name = "news/delete.html"
    success_url = "/news/"

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
