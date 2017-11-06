from django.shortcuts import render
def overview(request):
    return render(request, 'website/overview.html', {})
def about(request):
    return render(request, 'website/about.html', {})
def details_AS_UK(request):
    return render(request, 'website/details_AS_UK.html', {})
def details_AS_DE(request):
    return render(request, 'website/details_AS_DE.html', {})
def details_TAB_UK(request):
    return render(request, 'website/details_TAB_UK.html', {})
def details_TAB_DE(request):
    return render(request, 'website/details_TAB_DE.html', {})
#def home(request):
#    return render(request, 'website/home.html', {})
#def participate(request):
#    return render(request, 'website/participate.html', {})
#def previewNL(request):
#    return render(request, 'website/previewNL.html', {})
#def previewUK(request):
#    return render(request, 'website/previewUK.html', {})
#def UK(request):
#    return render(request, 'website/UK.html', {})