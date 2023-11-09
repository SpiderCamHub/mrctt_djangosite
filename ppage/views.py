from django.shortcuts import render

# Create your views here.

def ppage(request):
    return render(request, 'ppage/home.html',{})

