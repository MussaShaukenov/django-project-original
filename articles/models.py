from django.db import models
from django.urls import reverse

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('view_articles', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Statistics(models.Model):
    city = models.CharField(max_length=255)
    number_of_infected_with_pcr_plus = models.IntegerField(default=0)
    number_of_infected_with_pcr_minus = models.IntegerField(default=0)
    number_of_recovered = models.IntegerField(default=0)
    number_of_infected_expected = models.IntegerField(default=0)
    number_of_recovered_expected = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    @property
    def number_of_infected_with_pcr_total(self):
        return self.number_of_infected_with_pcr_plus + self.number_of_infected_with_pcr_minus

    def get_absolute_url(self):
        return reverse('statistics', kwargs={'city': self.pk})

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'
        ordering = ['city']

