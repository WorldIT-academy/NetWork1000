from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"

    def clean_name(self):
        '''
            Валідатор, що пов'язаний з полем name та перевіряє, чи ім'я тегу починається з літеру
        '''
        name = self.cleaned_data.get("name")
        if not name[0].isalpha():
            raise ValidationError("Ім'я тегу повинно починатись з літери, а не з символу або цифри")
        return name
    

    def clean(self):
        '''
            Валідатор, що не пов'язаний з полем name та перевіряє, якщо тег є активним, то іконка та 
            опис мають бути вказаними
        '''
        is_active = self.cleaned_data.get("is_active")
        icon = self.cleaned_data.get("icon")
        description = self.cleaned_data.get("description")
        
        if is_active:
            if not icon or not description:
                raise ValidationError("Іконка та опис є обов'язковими, якщо створюється активний тег")
            
        return self.cleaned_data
        
        
# Створюємо клас для форми, що є пов'язаною з моделлю
class PostForm(forms.ModelForm):
    # Клас, що відповідає за налаштування форми
    class Meta:
        # Пов'язуємо форму з моделлю
        model = Post
        # Поля форми, що будуть відображатись на сторінці
        fields = ["title", "content", "image", "tags"]
        # Кастомізація полів
        widgets = {
            "title": forms.TextInput(attrs={"id": 'title',"class": "title","placeholder":"Заголовок"}),
            'content': forms.Textarea(attrs={'class': 'content'})
        }
        # Вказуємо кастомні повідомлення для пвених помилок для кожного поля
        error_messages = {
            "title": {
                "required": "Це поле обов'язкове для заповнення",
                "max_length": "Введено більше, ніж 255 символів"
            },
            'content':{
                'required': "Введіть контент!"
            }
        }
    # Перезаписуємо вже існуючий метод save(), для збереження автора та тегів
    def save(self, author):
        # Створємо об'єкт поста
        post = super().save(commit=False)
        # Підв'язуємо та зберігаємо автора
        post.author = author
        post.save()
        # Підв'язуємо та зберігаємо теги
        post.tags.set(self.cleaned_data.get("tags"))
        post.save()
