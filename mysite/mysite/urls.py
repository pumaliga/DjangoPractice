from django.contrib import admin
from django.urls import path, re_path, include
from myapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('articles/', articles, name='articles'),
    path('acrticles/archive', archive, name='archive'),
    path('users/', users, name='users'),
    path('article/<int:art_num>/', article, name='article'),
    path('article/<int:art_num>/archive', archive, name='article_arc'),
    path('article/<int:art_num>/<slug:slug_text>', slug_text, name='slug_text'),
    path('users/<int:user_number>/', users_num, name='us-num'),
    re_path(r'\b050\d{7}\b|066\d{7}\b|099\d{7}\b|095\d{7}\b|'
            r'067\d{7}\b|068\d{7}\b|096\d{7}\b|097\d{7}\b|'
            r'098\d{7}\b|063\d{7}\b|073\d{7}\b|093\d{7}\b|089\d{7}\b|094\d{7}\b',
            number),
    re_path(r'\b[a-f0-9]{4}[-]{1}[a-f0-9]{6}\b', last_url)
]
