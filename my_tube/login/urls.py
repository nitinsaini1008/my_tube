from . import views
from django.urls import path

urlpatterns = [
	path('',views.home,name='home'),
	path('showvideo',views.showvideo,name='showvideo'),
	path('add',views.add,name='add'),
	path('show',views.show,name='show'),
	path('showphotos',views.showphotos,name='showphotos'),
]