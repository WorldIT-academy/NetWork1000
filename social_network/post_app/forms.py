from django import forms
from .models import Post

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
