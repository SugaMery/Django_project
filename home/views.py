from .forms import UsersForm
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _

# Create your views here.
from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext



def index(request):
    return render(request,'home/index.html')

def contact(request):
    return render(request,'home/contact.html')  

def admistration(request):
    return render(request,'home/admistration.html')

def registerPage(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsersForm()
        return render(request , 'home/index.html' , {'form' : form}) 


def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')

		context = {}
		return render(request, 'home/index.html', context)           

def logoutUser(request):
	logout(request)
	return redirect('login')

