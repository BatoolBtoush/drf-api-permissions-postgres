from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class TestMusicView(TestCase):

    def setUp(self):
        self.client.login(username="batool", password="12345")
    
    def test_authetication_required(self):
        self.client.logout()
        url = reverse('musics-list')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



