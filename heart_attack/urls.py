from django.conf.urls import url
from .import views

app_name = 'heart_attack'

urlpatterns = [
    url(r'^$', views.index, name ='index'),
	 url(r'^insertuser/$',views.insertuser, name='insertuser')
	
]