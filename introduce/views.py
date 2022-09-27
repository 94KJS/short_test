from django.shortcuts import render
from introduce.models import AccessLog


def introduce(request):
    # case1
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()

    return render(request, 'introduce.html')