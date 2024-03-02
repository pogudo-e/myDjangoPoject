from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # не обязательно для заполнения
    created_at = models.DateTimeField(auto_now_add=True) # автоматическое заполнение один раз
    updated_at = models.DateTimeField(auto_now=True) # автоматическое заполнение каждое обновление
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title