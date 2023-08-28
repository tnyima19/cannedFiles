import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from UI.models import Message
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestMessageListPage(StaticLiveServerTestCase):


	def setUp(self):
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
		#chrome_options = webdriver.Chrome()
		firefox_driver = os.path.join(os.getcwd(),'geckodriver.exe')
		firefox_service = Service(firefox_driver)
		firefox_options = Options()
		firefox_options.set_preference('general.useragent.override',user_agent)
		self.browser = webdriver.Firefox(service=firefox_service, options=firefox_options)



	def tearDown(self):
		self.browser.quit()

	def test_create_message(self):
		self.browser.get(self.live_server_url)

		title_input = self.browser.find_element_by_id("title")
		title_input.send_keys("Title")

		#Find and Fill teh "line1" input field
		line1_input = self.browser.find_element_by_name("line1")
		line1_input.send_keys("Line 1 Content")
		time.sleep(5)

	# def test_create_message(self):
	# 	self.browser.get(self.live_server_url)
	# 	#wait = WebDriverWait(self.browser, 10)
	# 	search = self.browser.find_element_by_name("line1")
	# 	search.send_keys("Title")
	# 	search.send_keys(Keys.RETURN)
	# 	time.sleep(20)
		

	# def test_Message_exists_after_creation(self):
	# 	self.browser.get(self.live_server_url)

	# 	#user requests page for first time
	# 	search = self.browser.find_element(By.NAME,'title')
	# 	self.assertEquals(
	# 		alert.find_element_by_tag_name('h3')
		
	# 	)
	