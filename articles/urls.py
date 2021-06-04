from django.urls import path
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
   path('articles/', HomeArticles.as_view(), name='articles'),
   path('category/<int:category_id>/', ArticlesByCategory.as_view(), name='category'),
   path('articles/<int:pk>', ViewArticles.as_view(), name='view_articles'),
   path('articles/add_articles', CreateArticles.as_view(), name='add_articles'),
   path('statistics/', HomeStatistics.as_view(), name="forecasting")
]





