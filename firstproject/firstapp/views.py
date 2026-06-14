from django.shortcuts import render

def indexpage(request):
    return render(request,'index.html')

def secondpage(request):
    return render(request,'secondpage.html')