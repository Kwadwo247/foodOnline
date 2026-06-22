from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return HttpResponse("Hello World! Frank found the true way and he's is coming")
