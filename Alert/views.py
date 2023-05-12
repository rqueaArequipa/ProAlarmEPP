from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from django.http import HttpResponse

class IndexView(View):
    def get(self,request):
        #context = {'mensaje':'<Button>Click Aqui</Button>'}
        return HttpResponse('<Button style="background: black;"><a href="/api" style="text-decoration: none; color: white;">Click Aqui</a></Button>')
