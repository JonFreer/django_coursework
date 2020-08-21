from django.test import TestCase
from django.urls import resolve
from django.urls import reverse, resolve
from cv.views import cv_main
from django.http import HttpRequest

# Create your tests here.


class HomePageTest(TestCase):

       def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_main(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>CV</title>', html)  
        self.assertTrue(html.endswith('</html>'))  