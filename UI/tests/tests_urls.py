from django.test import SimpleTestCase
from django.urls import reverse, resolve
from UI.views import ( MessageListView,
					MessageDetailView,
 					MessageDeleteView,
 					MessageUpdateView,
					MessageCreateView,
					create_message,
					delete_message,
					canned_text )

class TestsUrls(SimpleTestCase):

	def test_home_url_is_resolved(self):
		url = reverse('main-home')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, MessageListView)
	

	def test_detail_url_is_resolved(self):
		message_pk = 12
		url = reverse('message-detail',kwargs={'pk': message_pk})
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, MessageDetailView)

	def test_message_update_url_is_resolved(self):
		message_pk = 12
		url = reverse('message-update',kwargs={'pk': message_pk})
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, MessageUpdateView)

	def test_create_message(self):
		url = reverse('create_message')
		print(resolve(url))
		self.assertEquals(resolve(url).func, create_message)