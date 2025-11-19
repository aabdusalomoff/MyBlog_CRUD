from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.FileField(upload_to="image")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    