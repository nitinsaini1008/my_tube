from django.shortcuts import render
from django.http import HttpResponse
from .models import photos
from .models import Video
from .forms import VideoForm
from .forms import photoForm
# Create your views here.
def home(request):
	i=photos.objects.all()
	return render(request,'login.html',{'i':i})

def add(request):
	a=request.POST['a']
	b=request.POST['b']
	c=int(a)+int(b)
	return render(request,'ans.html',{'result':c})


def showvideo(request):

    lastvideo= Video.objects.last()

    videofile= Video.objects.all()


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'videofile': videofile,
              'form': form
              }
    
      
    return render(request, 'videos.html', context)


def show(request):
  i=Video.objects.all()
  return render(request,'show.html',{'i':i})
def showphotos(request):
    lastvideo= photos.objects.last()

    videofile= photos.objects.all()
    form= photoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()  
    context= {'videofile': videofile,
              'form': form
              }
    return render(request, 'photo.html',context)