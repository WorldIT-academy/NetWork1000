from .views import *
from django.urls import path


urlpatterns = [
    path('registration/', render_registration),
    path('login/', render_login, name="login"),
    path('welcome/', render_welcome, name='welcome'),
    path('logout_user/', logout_user, name = 'logout'),
    path('all_profiles/', render_profiles,name='all_profiles')
]

