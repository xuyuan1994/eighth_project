from django.shortcuts import render
def index(request):
    return render(request,'register/index.html')
def register0(request):

    return render(request,'register/result.html')
# Create your views here.
