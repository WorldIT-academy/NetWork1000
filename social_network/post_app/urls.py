from .views import *
from django.urls import path


urlpatterns = [
    path('all/', render_all_posts)
]