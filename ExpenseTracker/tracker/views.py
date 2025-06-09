from django.shortcuts import render
from django.http import HttpResponse
from .models import Session
def Home(request):
    print(request.method)
    Session.objects.create(req_type = str(request.method))
    sessions = Session.objects.all()
    data = list(sessions.values())
    return HttpResponse(f"{data}")
# Create your views here.
