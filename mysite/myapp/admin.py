from django.contrib import admin
from .models import Article, DislikeToComment, LikeToComment, CommentToArticle, LikeToArticle, DislikeToArticle
from .models import MyUser

admin.site.register(Article)
admin.site.register(CommentToArticle)
admin.site.register(LikeToComment)
admin.site.register(DislikeToComment)
admin.site.register(LikeToArticle)
admin.site.register(DislikeToArticle)
admin.site.register(MyUser)
