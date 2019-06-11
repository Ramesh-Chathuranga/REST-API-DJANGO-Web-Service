from django.test import TestCase
from django.shortcuts import render,HttpResponse
# Create your tests here.
def index(req):
    print("hi")
    # return HttpResponse("hi")
    return render(req,"miriapp/index.html",{"hi":"Ramesh HI"})