from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from django.http import HttpResponse

from django.shortcuts import render

def IndexView(request):
    return render(request, 'index.html')
