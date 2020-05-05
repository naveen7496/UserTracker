from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, ActivityPeriod
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


def user_details(request):
    users = User.objects.all()
    details = []
    for user in users:
        member = {}
        user_profile = get_object_or_404(Profile, user=user)
        activity_periods_of_user = ActivityPeriod.objects.filter(user=user)
        periods_of_user = [] # in string format
        for period in activity_periods_of_user:
            period_dict = {}
            start_time = period.start_time.strftime("%b-%d-%Y %H:%M:%S %p")
            end_time = period.end_time.strftime("%b-%d-%Y %H:%M:%S %p")
            period_dict = {
                "start_time": start_time,
                "end_time": end_time
            }
            periods_of_user.append(period_dict)
        member = {
            "id": user.id,
            "real_name": user_profile.real_name,
            "tz": user_profile.tz,
            "activity_periods": periods_of_user
        }
        details.append(member)
    data = json.dumps(details)
    return JsonResponse(data, safe=False)


