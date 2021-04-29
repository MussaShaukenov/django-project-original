from django import forms
from .models import Articles
import re
from django.core.exceptions import ValidationError


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    #  VALIDATOR
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title name cannot be started with a Number')
        return title

