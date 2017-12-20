# coding=utf-8

from django.test import TestCase, Client
#from django.core.urlresolvers import reverse #-- codigo do aula nao deu certo
from django.urls import reverse# usando este deu certo

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

