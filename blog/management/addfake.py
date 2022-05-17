from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Follower, Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        # self.create_user()
        # self.create_follower()
        self.create_post()
        self.stdout.write('Success')

    def create_user(self):
        for i in range(2000):
            user = User.objects.create(
                username=f"test {i+7}",
            )
            user.set_password('dhsfyudheyjrekjrefnnfevjjves')
            user.save()

    def create_follower(self):
        user_list = User.objects.order_by()[2:]
        for user in user_list:
            Follower.objects.create(user=user, subscriber_id=1)

    def create_post(self):
        user_list = User.objects.all()
        for user in user_list:
            for i in range(500):
                Post.objects.create(text=f"Test post{i}", user=user)