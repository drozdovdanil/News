from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Имя')
    rating = models.IntegerField(default=0)

    def update_rating(self):
        rating_of_posts_by_author = Post.objects.filter(author=self).aggregate(Sum('rating'))['rating_sum'] * 3
        rating_of_comments_by_author = Comment.objects.filter(user=self.user).aggregate(Sum('rating'))['rating_sum']
        rating_of_comments_posts_by_author = Comment.objects.filter(post__author__user=self.user).aggregate(Sum('rating'))['rating_sum']

        self.rating = rating_of_comments_by_author + rating_of_posts_by_author + rating_of_comments_posts_by_author
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    news = 'NE'
    article = 'AR'

    type_1 =[(news, 'Новость'),
            (article, 'Статья')]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_1 = models.CharField(max_length=255, choices=type_1)
    time_post = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text_news = models.TextField()
    rating_news = models.IntegerField(default=0)

    def like(self):
        self.rating_news + 1
        self.save()

    def dislike(self):
        self.rating_news - 1
        self.save()

    def preview(self):
        return self.text_news[0:125] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment + 1
        self.save()

    def dislike(self):
        self.rating_comment - 1
        self.save()
