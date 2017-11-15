from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

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

def	new_topic(request):
	"""用户添加主题"""
	if request.method != "POST":
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("llapp1:topics"))
	context = {"form":form}
	return render(request,"new_topic.html",context)

def	new_entry(request,topic_id):
	"""在特定的主题中添加条目"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != "POST":
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse("llapp1:topic",args=[topic_id]))

	context = {"topic":topic,"form":form}
	return render(request,"new_entry.html",context)

def edit_entry(request,topic_id):
	"""编辑现有的条目"""
	entry = Entry.objects.get(id=topic_id)
	topic = entry.topic

	if request.method != "POST":
		# 初次请求，使用当前条目填充表单
		form = EntryForm(instance=entry)
	else:
		# post提交，对数据进行处理
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("llapp1:topic",args=[topic_id]))

	context = {"entry":entry,"topic":topic,"form":form}
	return render(request,"edit_entry.html",context)
# Create your views here.
