from django.test import TestCase, Client
from django.urls import reverse
from UI.models import Message
from UI.views import create_message, delete_message
import json
from datetime import datetime


class TestViews(TestCase):
	def setUp(self):
		#self.client = Client()
		#self.list_url = reverse('main-home')
		#self.message_pk = 12
		#self.detail_url = reverse('message-detail',kwargs={'pk': message_pk})
		self.message = Message.objects.create(title='Test Message', line1='line1',display_time=5)


	def test_home_view_GET(self):
		list_url = reverse('main-home')
		response = self.client.get(list_url)
		self.assertEquals(response.status_code, 200)
		self.assertContains(response, 'Test Message')
		self.assertTemplateUsed(response, 'UI/UI.html')

	def test_create_message_view_GET(self):
		#message_pk = 41
		data = {'title':'New Message', 'line1':'New Line 1','display_time':5}
		list_url = reverse('create_message')
		response = self.client.post(list_url, data)
		self.assertEquals(response.status_code, 302)
		self.assertEqual(Message.objects.count(), 2) # check if  new message was created
		#self.assertTemplateUsed(response, 'UI/message_detail.html')


	def test_delete_message_view(self):
		response = self.client.post(reverse('message-delete',args=[self.message.id]))
		#response = self.client.post(reverse('message-delete', args=[self.message.id]))
		self.assertEquals(response.status_code, 302)
		self.assertEquals(Message.objects.count(), 0)

	def test_canned_text_view(self):
		url = reverse('canned_text')
		response = self.client.get(url)
		self.assertEqual(response['Content-Type'], 'text/plain')
		self.assertTrue('attachment; filename=canned.rte' in response['Content-Disposition'] )
		#self.assertContains(response, 'Test Message')
		#self.assertContains(response, 'Line 1 of Message 1')