from django.shortcuts import redirect

def redirect_index(request):
	return redirect('index_url', permanent = True)