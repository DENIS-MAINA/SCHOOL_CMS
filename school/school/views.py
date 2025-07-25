from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, I am [DENIS MAINA IRUNGU]</h1><p>My favorite quote is: 'Nice guys , always finish last.'</p>")
