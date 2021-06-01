from django.contrib import admin
from .models import Articles, Category, Statistics


# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'number_of_infected_with_pcr_plus', 'number_of_infected_with_pcr_minus',
                    'number_of_infected_with_pcr_total', 'number_of_recovered', 'number_of_infected_expected',
                    'number_of_recovered_expected', 'date')
    list_display_links = ('id', 'city')
    search_fields = ('city', 'id')


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
