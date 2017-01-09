from django.test import TestCase
from django.core.urlresolvers import reverse

from app.models import User


class UserTest(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'test',
            'birthday': '2017-02-02',
            'password': 'test'
        }

    def test_create_user(self):
        resp = self.client.post(reverse('user_create'),
                                data=self.user_data, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'User List', 1)

    def test_invalid_create_user(self):
        data = self.user_data
        data['username'] = ''

        resp = self.client.post(reverse('user_create'), data=data, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'User List', 0)

    def test_user_list(self):
        resp = self.client.get(reverse('user_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'User List', 1)

    def test_user_detail(self):
        user = User.objects.create_user(**self.user_data)

        resp = self.client.get(reverse('user_detail', args=[user.id]))
        self.assertEqual(resp.status_code, 200)

    def test_user_delete(self):
        user = User.objects.create_user(**self.user_data)

        resp = self.client.post(
            reverse('user_delete', args=[user.id]), follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'User List', 1)

    def test_invalid_user_delete(self):
        resp = self.client.post(reverse('user_delete', args=[1]), follow=True)

        self.assertEqual(resp.status_code, 404)
