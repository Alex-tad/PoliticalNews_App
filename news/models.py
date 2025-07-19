from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=500)
    summary = models.TextField()
    source = models.CharField(max_length=100)
    link = models.URLField()
    published = models.DateTimeField()
    tags = models.CharField(max_length=255, blank=True)
    language = models.CharField(
        max_length=10,
        choices=[('en', 'English'), ('am', 'Amharic')],
        default='en'
    )
    is_breaking = models.BooleanField(default=False)  # 🔥 Breaking news flag

    def __str__(self):
        return self.title

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    channel_title = models.CharField(max_length=100)
    video_id = models.CharField(max_length=50, unique=True)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
