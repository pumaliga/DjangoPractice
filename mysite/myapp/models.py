from django.db import models
from datetime import timedelta, datetime


class Author(models.Model):
    name = models.CharField(max_length=120)


class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)

    def str(self):
        return f'Name - \"{self.name}\" Author - \"{self.author}\"'


class CommentToArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    comment_to_comment = models.ForeignKey('myapp.CommentToArticle', null=True, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now)

    def save(self, **kwargs):
        if not self.id:
            self.created_at = datetime.now() - timedelta(days=365)
        super().save(**kwargs)

    def str(self):
        if self.comment:
            return f'Comment #{self.id} Article - \"{self.article.name}\" from \"{self.author}\"'
        else:
            return f'Comment to comment {self.comment}!'


class LikeToComment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Like 👍 - comment #{self.comment.id} from \"{self.author}\"'


class DislikeToComment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentToArticle, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Dislike 👎🏻 - comment #{self.comment.id} from \"{self.author}\"'


class LikeToArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Like 👍 - Article #{self.comment.id} from \"{self.author}\"'


class DislikeToArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Dislike 👎🏻 - Article #{self.comment.id} from \"{self.author}\"'