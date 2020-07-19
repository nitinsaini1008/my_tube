from django.db import models

# Create your models here.
class photos(models.Model):
	name=models.CharField(max_length=100)
	desc=models.CharField(max_length=100)
	img=models.FileField(upload_to='pics')


class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='all_videos', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
