from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .forms import NewsLetterForm, CustomUserCreationForm, WalkInForm
from .models import Clients, Openings, ContactUs


def home(request):
    clients = Clients.objects.all()
    return render(request, 'home.html', {'clients': clients})

def signup_user(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password1'),
                    email=request.POST.get('email')
                )
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'signup_user.html', {'form': CustomUserCreationForm(),
                                                            'error': 'That username has already been taken. '
                                                                     'Please choose a new username'})
        else:
            return render(request, 'signup_user.html',
                          {'form': CustomUserCreationForm(), 'error': 'Passwords did not match'})
    return render(request, 'signup_user.html', {'form': CustomUserCreationForm()})


def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return render(request, 'login_user.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'login_user.html', {'form': AuthenticationForm()})

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

def add_mail(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = NewsLetterForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

def contactus(request):
    if request.method == 'POST':
        data = request.POST
        contact = ContactUs(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        contact.save()
        return redirect('Home')
    return render(request, 'contactus.html')


def life_at_arise(request):
    return render(request, 'life_at_arise.html')

def why_arise_solution(request):
    return render(request, 'why_arise_solution.html')

def applicationprocess(request):
    return render(request, "applicationprocess.html")

def awards(request):
    return render(request, "awards.html")

def careers(request):
    return render(request, "careers.html")

def apprenticeship(request):
    return render(request, "apprenticeship.html")

def bulkrecruit(request):
    return render(request, "bulkrecruit.html")

def contractstaff(request):
    return render(request, "contractstaff.html")
    
def employeelease(request):
    return render(request, "employeelease.html")

def hiretraindeploy(request):
    return render(request, "hiretraindeploy.html")

def itstaff(request):
    return render(request, "itstaff.html")

def leadership(request):
    return render(request, "leadership.html")

def payroll(request):
    return render(request, "payroll.html")

def permstaff(request):
    return render(request, "permstaff.html")

def turnkey(request):
    return render(request, "turnkey.html")

def walk_in_form(request):
    if request.method == 'POST':
        try:
            form = WalkInForm(request.POST)
            form.save()
            return redirect('Home')
        except MultiValueDictKeyError:
            return render(request, 'walkinform.html', {'error': 'All fields are compulsory'})
    return render(request, 'walkinform.html', {'jobs': Openings.objects.filter(display=True)})
