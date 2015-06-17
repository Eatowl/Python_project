from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth 

def login(request):
	slov = {}
	slov.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			slov['login_error'] = "not user"
			return render_to_response('register.html', slov)
	else:
		return render_to_response('register.html', slov)

def logout(request):
	auth.logout(request)
	return redirect('/')

def register(request):
	slov = {}
	slov.update(csrf(request))
	slov['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/')
		else:	
			slov['form'] = newuser_form
	return render_to_response('regist.html', slov)
