from django import forms

from books.models import coment


class CommentForm(forms.ModelForm):
    class Meta:
        model=coment
        fields=('text',)
