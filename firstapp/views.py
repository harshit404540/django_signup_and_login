from django.shortcuts import render,redirect
from datetime import datetime 
from firstapp.models import Signup
from django.contrib import messages 
import random
from django.core.mail import send_mail
import string

# Create your views here.
def home(request):
	return render(request,'home.html')

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
	
def signup(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		date_time = datetime.today()
		secretkey = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
		data = Signup.objects.all()
		users = []
		emails = []
		for i in data:
			users.append(i.username)
			emails.append(i.email)
		if password1 == password2:
			passwords = password2
			if username not in users and email not in emails:
				signup_form = Signup(fname = fname, lname = lname, email = email, username = username, password = passwords, date_time = date_time,secret_key = secretkey)
				signup_form.save()
				send_mail(
				subject='Secret key',
				message=f'Your secret key:{secretkey}\nUser:{username} , use it for login and keep it safe /within you',
				from_email='Your_mail',
				recipient_list=[f'{email}'],
				fail_silently=False,
				)
				messages.success(request,f"Signup Successfully, You can now login...")	
				messages.success(request,f'Secret key sent to {email}, keep it safe and dont share it with anyone...')
				return redirect('signup')
			else:
				if username in users:
					messages.error(request, 'Username already taken')
				if email in emails:
					messages.error(request, 'Account already registered with this email. Try another email...\n')
				return redirect('signup')
		else:
			messages.error(request,"Password doesn't match...")
			return redirect('signup')
	return render(request,'signup.html')

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		secretkey = request.POST.get('secretkey')
		password = request.POST.get('password')
		data = Signup.objects.all()
		emails = []
		passkey = []
		key = []
		for i in data:
			emails.append(i.email)
			passkey.append(i.password)
			key.append(i.secret_key)
		if email in emails and password in passkey :
			arg = True
		if secretkey in key and arg is True:
			messages.success(request,"Login Successfully...")
			return redirect('login')
		else:
			if email not in emails and password not in passkey:
				messages.error(request,"Account does not exist...")
			if secretkey not in key:
				messages.error(request,"Invalid secret key...")
			return redirect('login')
	return render(request,'login.html')

def login_with_username(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		secretkey = request.POST.get('secretkey')
		data = Signup.objects.all()
		users = []
		passkey = []
		key = []
		for i in data:
			users.append(i.username)
			passkey.append(i.password)
			key.append(i.secret_key)
		if username in users and password in passkey :
			arg = True
		if secretkey in key and arg is True:
			messages.success(request,"Login Successfully...")
			return redirect('login_with_username')
		else:
			if username not in users and password not in passkey:
				messages.error(request,"Account does not exist...")
			if secretkey not in key:
				messages.error(request,"Input valid secret key associated with this account...")
			return redirect('login_with_username')
	return render(request,'login_with_username.html')
