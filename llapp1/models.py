from django.db import models


class Topic(models.Model):
	text = models.CharField(max_length=200)
	add_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

class Entry(models.Model):
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Entries"\

	def __str__(self):
		return self.text[:50]+"..."
# Create your models here.
