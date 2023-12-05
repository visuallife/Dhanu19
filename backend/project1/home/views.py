from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'Home.html')
def buy(request):
    return render(request,'items.html')
def about(request):
    return render(request,'blogs.html')
def login(request):
    return render(request,'acc.html')
def ar(request):
    return render(request,'ar.html')