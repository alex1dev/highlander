# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from club.forms import UserForm, SelEntForm, SelDepForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import datetime 
# Create your views here.
def index(request):
	return render(request, 'club/index.html')

def contact(request):
	return render(request, 'club/contact.html')

def example(request):
	return render(request, 'club/example.html')

def hotel(request):
	return render(request, 'club/hotel.html')

def landscapes(request):
	return render(request, 'club/landscapes.html')

def ulogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('index')
			else:
				return HttpResponse('Account is disabled')
		else:
			print('Invalid login details: {0}, {1}'.format(username, password))
			return HttpResponse("Invalid login details supplied")
	else:
		return render(request, 'club/login.html')

@login_required
def ulogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()

	return render(request, 'club/register.html', {'user_form':user_form, 'registered':registered})


e_d=""
d_d=""

@login_required
def booking(request):
    global e_d
    global d_d
    
    if request.method == 'POST':
        edateform = SelEntForm(data=request.POST)
        ddateform = SelDepForm(data=request.POST)

        if edateform.is_valid() & ddateform.is_valid():
            e_d = edateform.cleaned_data['entrance_date']
            d_d = ddateform.cleaned_data['departure_date']
            print(e_d)
            print(d_d)
            return HttpResponseRedirect(reverse('congrat') )

    
    else:
        proposed_entrance_date = datetime.date.today() + datetime.timedelta(weeks=3)
        edateform = SelEntForm(initial={'entrance_date': proposed_entrance_date,})
      	proposed_departure_date = datetime.date.today() + datetime.timedelta(weeks=4)
      	ddateform = SelDepForm(initial={'departure_date' : proposed_departure_date,})
    return render(request, 'club/booking.html', {'edateform': edateform, 'ddateform': ddateform, 'ed':e_d, 'dd':d_d})

@login_required
def congrat(request):

	global e_d
	global d_d

	print(e_d)
	print(d_d)

	return render(request, 'club/congrat.html', {'ed':e_d, 'dd':d_d})