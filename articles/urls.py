from django.urls import path
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
   path('register/', register, name="register"),
   path('login/', user_login, name="login"),
   path('logout/', user_logout, name="logout"),
   path('', statistiscs, name='statistics'),
   path('', index, name="home"),
   path('articles/', listing_articles, name='articles'),
   path('category/<int:category_id>/', ArticlesByCategory.as_view(), name='category'),
   path('articles/<int:pk>', ViewArticles.as_view(), name='view_articles'),
   path('subs/', subs, name='subs'),
   path('add_articles/', CreateArticles.as_view(), name='add_articles'),
]








