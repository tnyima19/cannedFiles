from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (MessageListView, 
	MessageDetailView,
	MessageCreateView,
	MessageUpdateView, 
	MessageDeleteView,
	create_message,
	delete_message)


urlpatterns = [
	path('', MessageListView.as_view(), name='main-home'),
	path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
	path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
	path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message-update'),
	path('create_message/', views.create_message, name='create_message'),
	#MESSAGER CREATE VIEW
	#path('message/new/', MessageCreateView.as_view(), name='message-create')
	path('about/',views.about, name='main-about'),
	path('login/', auth_views.LoginView.as_view(template_name='UI/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='UI/logout.html'), name='logout'),
	path('canned_text', views.canned_text, name='canned_text'),
]