from django.contrib.auth.models import Group
from django.contrib.auth.signals import user_logged_in


def setup_user(sender, request, user, **kwargs):
    """
    Make sure all users are in a common group and can log into the admin.

    This makes setting up permissions in the crud admin easier.
    """
    if not user.is_staff:
        group = Group.objects.get(name='users')  # XXX magic constant
        user.groups.add(group)
        user.is_staff = True
        user.save()
        # TODO log


user_logged_in.connect(setup_user)
