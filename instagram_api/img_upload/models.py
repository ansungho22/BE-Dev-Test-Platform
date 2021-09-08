from django.db import models

# Create your models here.


class Instagram(models.Model):
    UploadTime = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    context = models.TextField(max_length=400)
    photo_URL = models.TextField()
    

    class Meta:
        ordering = ["UploadTime"]

    def __str__(self):
        return self.Title