from django import forms
from .models import Tag


class PostForm(forms.Form):
    title = forms.CharField(
        max_length = 255, 
        required = True, 
        widget = forms.TextInput(attrs = {"placeholder":"Заголовок"})
        )
    content = forms.CharField(
        widget = forms.Textarea(attrs = {"placeholder":"Контент"}), 
        required = True
        )
    image = forms.ImageField(required= True)
    tags = forms.ModelMultipleChoiceField(
        queryset= Tag.objects.all(),
        widget = forms.SelectMultiple(),
        required = False
    )