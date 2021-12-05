from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    date = models.DateField()
    thumbnail = models.ImageField(upload_to='post')
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
       ordering = ['-date']
