from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Category, Statistics
from django.urls import reverse_lazy

from .forms import ArticlesForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class HomeArticles(ListView):
    model = Articles
    template_name = 'articles/home_articles_list.html'
    context_object_name = 'articles'  # the name instead of default object_list in for loop in home_news_list.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return Articles.objects.filter(is_published='True')


class ArticlesByCategory(ListView):
    model = Articles
    template_name = 'articles/home_articles_list.html'
    context_object_name = 'articles'
    allow_empty = False  # default True | prohibits displaying empty lists on the page

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Articles.objects.filter(category_id=self.kwargs['category_id'],
                                       is_published='True')


class ViewArticles(DetailView):
    model = Articles
    # pk_url_kwarg = 'article_id'
    # template_name = 'articles/articles_detail.html' by default
    context_object_name = 'articles_item'


class CreateArticles(CreateView):
    form_class = ArticlesForm  # select the class from the forms.py
    template_name = 'articles/articles_detail.html'
    success_url = reverse_lazy('home')  # get_absolute_url makes it automatically


def stats(request):
    return render(request, 'articles/statistics.html')




