from django import forms
from .models import Blog

class CommentForm(forms.Form):
    name = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=256)
    message = forms.CharField(max_length=500)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = "__all__"
        fields = ["title" , "description" , "content" , "author" , "category" , "Tag"]