from django.test import TestCase
from django.urls import resolve
from django.urls import reverse, resolve
from cv.views import cv_main
from django.http import HttpRequest
from cv.models import Course, Languages, Skills

# Create your tests here.


class HomePageTest(TestCase):

       def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_main(request)  
        html = response.content.decode('utf8')  
        self.assertIn('<title>CV</title>', html)  
        self.assertTrue(html.endswith('</html>'))  

class TestCourse(TestCase):

       def setUp(self):
              Course.objects.create(title = "TestCase" , grade="99", year="year2")

       def test_course(self):
              test_course = Course.objects.get(title = "TestCase")
              self.assertEqual(test_course.grade ,"99")

class TestLang(TestCase):

       def setUp(self):
              Languages.objects.create(title = "TestCase" , experience="lots")

       def test_course(self):
              test_lang = Languages.objects.get(title = "TestCase")
              self.assertEqual(test_lang.experience ,"lots")

class TestSkills(TestCase):

       def setUp(self):
              Skills.objects.create(title = "TestCase" , experience="lots" ,description = "test_desc")

       def test_course(self):
              test_skill = Skills.objects.get(title = "TestCase")
              self.assertEqual(test_skill.experience ,"lots")
              self.assertEqual(test_skill.description ,"test_desc")
