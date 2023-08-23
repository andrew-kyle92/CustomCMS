from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models.models import Page


# Create your tests here.
class PageAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.page_data = {'title': 'Test Page', 'content': 'This is a test page.'}
        self.page = Page.objects.create(**self.page_data)

    def test_create_page(self):
        response = self.client.post('/api/pages/', self.page_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_get_page(self ):
        response = self.client.get(f'/apis/pages/{self.page.id}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['title'], self.page_data['title'])
