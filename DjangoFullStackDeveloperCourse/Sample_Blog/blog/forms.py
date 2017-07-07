from django import forms
from blog.models import Posts,Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('author','title','text')

        widgets = {
        'title' : forms.TextInput(attrs={'class':'textinputclass'}),
        'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('author','text')

        widgets = {
        'author' : forms.TextInput(attrs={'class':'textinputclass'}),
        'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
