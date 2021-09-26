from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.

def articles_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename }'

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = ProcessedImageField(
        blank = True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90},
        upload_to='images/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
