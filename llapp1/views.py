from django.shortcuts import render
from .models import Topic

def index(request):
	"""学习笔记主页"""
	return render(request,"index.html")

def topics(request):
	"""主题（数据库表）"""
	topics = Topic.objects.order_by("add_time")
	context = {"ts":topics}
	return render(request,"topics.html",context)

def topic(request,topic_id):
	"""显示单个主题及其所有的条目(每一个数据记录)"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by("-date_add")
	context = {'topic':topic,'entries':entries}
	return render(request,'topic.html',context)

# Create your views here.
