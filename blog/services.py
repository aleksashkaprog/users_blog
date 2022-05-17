from django.conf import settings

from blog.models import Post


class Feed:
    """
    Service feeds
    """
    def get_post_list(self, user: settings.AUTH_USER_MODEL):
        return Post.objects.filter(user__owner__subscriber=user).order_by('-create_time')\
            .select_related('user')[:500]

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').get(id=pk)


feed_service = Feed()