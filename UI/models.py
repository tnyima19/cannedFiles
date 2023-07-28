from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
	title= models.CharField(max_length=20)
	line = models.TextField()
	#line2 = models.TextField()
	#line3 = models.TextField()
	#line4 = models.TextField()
	#line5 = models.TextField()
	#line6 = models.TextField()
	#line7 = models.TextField()
	display_time = models.IntegerField()
	transition_time = models.IntegerField()
	scroll= models.CharField(max_length=20)
	flash = models.BooleanField(default=False)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
