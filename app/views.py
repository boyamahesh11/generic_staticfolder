from django.shortcuts import render

# Create your views here.

def generic_static(request):
    return render(request,'generic_static.html')

def g2(request):
    return render(request,'g2.html')
