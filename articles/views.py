from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Category, Statistics
from .forms import ArticlesForm, UserRegisterForm, UserLoginForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome!')
            return redirect('login')
        else:
            messages.error(request, 'Something gone Wrong :(')
    else:
        form = UserRegisterForm()
    return render(request, 'articles/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'articles/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def statistiscs(request):
    objects = Statistics.objects.all()
    return render(request, 'articles/statistics.html', {'statistics': objects})

def index(request):
    return render(request, 'base.html')

def subs(request):
    return render(request, 'articles/subs.html')

# class HomeArticles(ListView):
#     model = Articles
#     template_name = 'articles/home_articles_list.html'
#     context_object_name = 'articles'  # the name instead of default object_list in for loop in home_news_list.html
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Main page'
#         return context
#
#     def get_queryset(self):
#         return Articles.objects.filter(is_published='True')


class ArticlesByCategory(ListView):
    model = Articles
    template_name = 'articles/home_articles_list.html'
    context_object_name = 'articles'
    allow_empty = False  # default True | prohibits displaying empty lists on the page
    paginate_by = 3

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
    form_class = ArticlesForm
    template_name = 'articles/add_articles.html'
    success_url = reverse_lazy('home')

def listing_articles(request):
    articles = Articles.objects.all()
    paginator = Paginator(articles, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/home_articles_list.html', {'page_obj': page_obj})

