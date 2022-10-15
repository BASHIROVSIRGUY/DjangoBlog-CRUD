from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, default='User')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['created_date']


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['updated_date']


class Comment(models.Model):
    text = models.TextField(max_length=300, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING, to_field='id')
    post = models.ForeignKey(Post, blank=False, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return "user:{user_id}, post:{post_id}, date: {created_date}" \
                .format(user_id=self.user.pk,
                        post_id=self.post.pk,
                        created_date=self.created_date)

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_date']