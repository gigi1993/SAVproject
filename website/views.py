from django.shortcuts import render

#def home(request):
#    return render(request, 'website/home.html', {})
#def participate(request):
#    return render(request, 'website/participate.html', {})
def overview(request):
    return render(request, 'website/overview.html', {})
def about(request):
    return render(request, 'website/about.html', {})
def previewNL(request):
    return render(request, 'website/previewNL.html', {})
def previewUK(request):
    return render(request, 'website/previewUK.html', {})
def UK(request):
    return render(request, 'website/UK.html', {})