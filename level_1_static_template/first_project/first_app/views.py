from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return HttpResponse("this is first project")
def index1(response):
    my_dict={'insert_me':'this is template'}
    return render(response,'index.html',context=my_dict)
