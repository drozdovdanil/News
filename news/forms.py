from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'category',
           'title',
           'text_news',

       ]

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get('title')
       content = cleaned_data.get('content')
       if title == content:
           raise ValidationError('The content shall differ from the title')
       return cleaned_data