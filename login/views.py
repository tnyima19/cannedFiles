from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def signin(request):
	form = 
	return render(request, 'login/login.html', {'form':form})
