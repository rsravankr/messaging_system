from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Message


class MessageTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_message_sending(self):
        self.client.login(username='user1', password='password')
        response = self.client.post('/api/messages/send/', {'receiver': self.user2.id, 'content': 'Hello'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.first().content, 'Hello')

    def test_message_thread(self):
        Message.objects.create(sender=self.user1, receiver=self.user2, content='Hi')
        Message.objects.create(sender=self.user2, receiver=self.user1, content='Hello')
        self.client.login(username='user1', password='password')
        response = self.client.get(f'/api/messages/thread/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
