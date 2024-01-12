from django.http import HttpResponse
from django.shortcuts import render
from . models import Stories

# Create your views here.
from PIL import Image



def index(request):
    obj=Stories.objects.all()

    return render(request,"index.html",{'result':obj})


