from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse




class UserApiTest(TestCase):
    def test_user_list_page(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_user_detail_page(self):
        url = reverse('user-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class PostTest(TestCase):
    def test_post_create_page(self):
        url = reverse('post-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_post_rud_page(self):
        url = reverse('post-rud', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_list_page(self):
        url = reverse('post-list', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class FollowerTest(TestCase):
    def test_follower_add_page(self):
        url = reverse('follow', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_followers_list_page(self):
        url = reverse('follower-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


class FeedTest(TestCase):
    def test_feed_page(self):
        url = reverse('feed', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_feed_timeline_page(self):
        url = reverse('feed-timeline')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

