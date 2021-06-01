from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Category, Statistics
from django.urls import reverse_lazy

from .forms import ArticlesForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from bs4 import BeautifulSoup
import requests


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


class StatisticsClass(ListView):
    model = Statistics
    template_name = 'articles/statistics.html'
    context_object_name = 'statistics'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Statistics Page'
        return context

    def get_queryset(self):
        return Statistics.objects.filter(city=self.kwargs['city'])

    def scrap_data(self):
        r = requests.get('https://www.coronavirus2020.kz/')
        content = r.content
        soup = BeautifulSoup(content, "lxml")
        data = []
        table = soup.find_all('table')[4]
        rows = table.find_all('tr', attrs={'class': ''})[1:]
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values
        d = []
        for row in data:
            d.append([{'city': row[0]}, {'NoI+': row[1]}, {'NoR': row[2]}, {'NoI-': row[4]}])

        return d



