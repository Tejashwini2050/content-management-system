from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255,null=False,blank=False)
    content= models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)

    def __str__(self):
        return self.title