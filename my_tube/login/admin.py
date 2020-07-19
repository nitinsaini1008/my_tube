from django.contrib import admin
from .models import photos
from .models import Video
# Register your models here.

admin.site.register(Video)
admin.site.register(photos)