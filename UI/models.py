from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Message(models.Model):
	title= models.CharField(max_length=20)
	line1 = models.TextField(max_length=17, null=True)
	line2 = models.TextField(max_length=17, null=True)
	line3 = models.TextField(max_length=17, null=True)
	line4 = models.TextField(max_length=17, null=True)
	line5 = models.TextField(max_length=17, null=True)
	line6 = models.TextField(max_length=17, null=True)
	line7 = models.TextField(max_length=17,null=True)
	line8 = models.TextField(max_length=17, null=True)
	transition_time1 = models.IntegerField(default=0)
	transition_time2 = models.IntegerField(default=0)
	transition_time3 = models.IntegerField(default=0)
	transition_time4 = models.IntegerField(default=0)
	transition_time5 = models.IntegerField(default=0)
	transition_time6 = models.IntegerField(default=0)
	transition_time7 = models.IntegerField(default=0)
	transition_time8 = models.IntegerField(default=0)
	scroll1= models.CharField(max_length=20, null=True)
	scroll2= models.CharField(max_length=20, null=True)
	scroll3= models.CharField(max_length=20, null=True)
	scroll4= models.CharField(max_length=20, null=True)
	scroll5= models.CharField(max_length=20, null=True)
	scroll6= models.CharField(max_length=20, null=True)
	scroll7= models.CharField(max_length=20, null=True)
	scroll8= models.CharField(max_length=20, null=True)
	flash1 = models.BooleanField(default=False)
	flash2 = models.BooleanField(default=False)
	flash3 = models.BooleanField(default=False)
	flash4 = models.BooleanField(default=False)
	flash5 = models.BooleanField(default=False)
	flash6 = models.BooleanField(default=False)
	flash7 = models.BooleanField(default=False)
	flash8 = models.BooleanField(default=False)
	display_time = models.IntegerField()
	voice_file_name = models.TextField(null=False, default='V500903')
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('message-detail', kwargs={'pk': self.pk})

