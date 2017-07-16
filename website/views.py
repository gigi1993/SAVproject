from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html', {})
def participate(request):
    return render(request, 'website/participate.html', {})
def overview(request):
    return render(request, 'website/overview.html', {})
def myfirstout(request):
    return render(request, 'website/myfirstout.html', {})
def line(request):
    return render(request, 'website/line.html', {})