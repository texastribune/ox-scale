from django.contrib.auth.models import Group
from django.contrib.auth.signals import user_logged_in


def setup_user(sender, request, user, **kwargs):
    """
    Make sure all users are in a common group.

    This makes setting up permissions in the crud admin easier.
    """
    group = Group.objects.get(name='users')  # XXX magic constant
    user.groups.add(group)


user_logged_in.connect(setup_user)
