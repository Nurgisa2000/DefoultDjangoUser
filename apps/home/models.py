from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField(upload_to='posts/') 
    description = models.TextField(max_length=499, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.author.username} - {self.pk}"

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
