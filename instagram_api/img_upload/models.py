from django.db import models

# Create your models here.


class Instagram(models.Model):
    Title = models.CharField(max_length=20)
    Context = models.TextField()
    UploadImage = models.URLField()
    UploadTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["UploadTime"]

    def __str__(self):
        return self.Title
