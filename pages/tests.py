from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

# Create your tests here.


class AboutUsPageTests(TestCase):

    def test_about_page_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us')

    def test_about_page_template_used(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')
