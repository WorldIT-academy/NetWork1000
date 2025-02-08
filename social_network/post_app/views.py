from django.shortcuts import render
from .models import Post
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os
from django.contrib.auth.decorators import login_required


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request, "post_app/all_posts.html", context={"all_posts": all_posts})

# Декоратор перевіряє, чи злогінився користувач. Якщо користувач на залогнився - перенаправляє на сторінку авторизації
@login_required
def render_create_post(request):
    if request.method == 'POST':
        # Отримуємо заголовок та контент з форми
        title = request.POST.get("title")
        content = request.POST.get("content")
        # Отримуємо файл зображення, яке користувач завантажив через форму
        image = request.FILES.get("image")
        # Шлях для береженян зобрежння у папці media
        image_path = os.path.join('images','posts', image.name)
        # Створюємо об'єкт файлової системи
        file_system = FileSystemStorage()
        # Зберігаємо зображення за вказаним шляхои
        file_system.save(name= image_path, content= image)

    return render(request, 'post_app/create_post.html')