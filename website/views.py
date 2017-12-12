from django.shortcuts import render
from .models import Click

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

def overview(request):
    return render(request, 'website/overview.html', {})
def about(request):
    return render(request, 'website/about.html', {})
def details_AS_UK(request):
	new_click = Click ()
	new_click.ip_address = get_ip(request)
	new_click.clicked = "UK"
	new_click.save()
	return render(request, 'website/details_AS_UK.html', {})
def details_AS_DE(request):
	new_click = Click ()
	new_click.ip_address = get_ip(request)
	new_click.clicked = "DE"
	new_click.save()
	return render(request, 'website/details_AS_DE.html', {})
	# new_click = Click ()
	# new_click.ip_address = get_ip(request)
	# new_click.clicked = "UK"
	# new_click.save()
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