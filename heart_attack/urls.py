from django.conf.urls import url
from .import views

app_name = 'heart_attack'

urlpatterns = [
    url(r'^$', views.index, name ='index'),
	url(r'^insert_user/$',views.insert_user, name='insert_user'),
    url(r'^result/$',views.result, name='result'),
]