'''定义llapp1的URL'''
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name="index")
]