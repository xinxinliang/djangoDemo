from django.db import models
from django.utils import timezone

class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = verbose_name_plural= "邮件"

    def __str__(self):
        return self.title
