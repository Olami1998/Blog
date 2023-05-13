from django import forms

from .models import Comment, News, Post




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title','slug',  'intro', 'body', 'image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        
        

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['email']