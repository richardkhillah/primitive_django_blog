from django import forms

from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),  # We must define this css class
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}), # we define postcontent, medium.com uses the other two css classes
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
