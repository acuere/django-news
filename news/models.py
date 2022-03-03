from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.title,
                # f"({self.created_at:%Y-%m-%d %H:%M}):"
                )
