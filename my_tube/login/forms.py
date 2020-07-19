from .models import Video
from .models import photos
from django import forms
class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]


class photoForm(forms.ModelForm):
    class Meta:
        model= photos
        fields= ["name", 'desc',"img"]
