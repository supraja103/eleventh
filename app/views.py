from django.shortcuts import render

# Create your views here.
def amma(request):
    return render(request,'amma.html')


def child(request):
    return render(request,'child.html')