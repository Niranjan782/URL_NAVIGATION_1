from django.shortcuts import render

# Create your views here.

def sample(request):
    return render(request,'sample.html')

def testing(request):
    return render(request,'testing.html')