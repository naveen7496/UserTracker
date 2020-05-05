from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from ... models import ActivityPeriod
from datetime import datetime


class Command(BaseCommand):
    help = 'It helps adding the activity period of a user'

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='+', type=str)

    def handle(self, *args, **options):
        arguments = options['arguments']
        fields = []
        for argument in arguments:
            fields.append(argument)
        user = User.objects.filter(username=fields[0])[0]
        start_time = datetime.strptime(fields[1], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(fields[2], "%Y-%m-%d %H:%M:%S")
        new_period = ActivityPeriod(user=user, start_time=start_time, end_time=end_time)
        new_period.save()
