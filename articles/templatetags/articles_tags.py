from django import template
from articles.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('articles/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}


