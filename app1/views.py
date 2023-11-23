from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def captain(request):
    return render(request,'captain.html')

def bowler(request):
    return render(request,'bowler.html')

def batman(request):
    return render(request,'batman.html')

def allrounder(request):
    return render(request,'allrounder.html')