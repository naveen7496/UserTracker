from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from ...models import Profile


class Command(BaseCommand):
    help = 'It helps creating a new user'

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='+', type=str)

    def handle(self, *args, **options):
        arguments = options['arguments']
        fields = []
        for argument in arguments:
            fields.append(argument)
        new_user = User.objects.create_user(username=fields[0], password=fields[1])
        new_user.save()
        profile_for_new_user = Profile(user=new_user, real_name=fields[2], tz=fields[3])
        profile_for_new_user.save()
        print('user created')

