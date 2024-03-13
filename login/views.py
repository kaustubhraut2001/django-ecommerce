from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import login

# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		# user = authenticate(request, username=username, password=password)
		# if user is not None:
		data = login.Object.create(username = username , password = password)
		data.save()

		if 1:
			# login(request, user)
            # Redirect to the products page
			return redirect('productspage')  # Assuming 'products:product_list' is the URL name for the products page
		else:
            # Authentication failed
			return HttpResponse("Invalid login credentials")
	else:
        # Render the login form
		return render(request, 'login.html')