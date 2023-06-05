from django.shortcuts import render, redirect
from .form import UserForm, TodoList
from .models import ListItem
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pin = request.POST['pin']
        user = authenticate(request, username=username, password=pin)
        if user is not None:
            auth_login(request, user)
            request.session.set_expiry(0)
            return redirect('todo')
        else:
            error_message = 'invalid username or pin'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pin = request.POST.get('pin')
        conpin = request.POST.get('conpin')

        if pin == conpin:
            try:
                user = User.objects.create_user(username=username, password=pin)
                return redirect('success')
            except IntegrityError:
                error_message = 'Username already taken'
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match'
            return render(request, 'signup.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')



def success(request):
    return render(request, 'success.html')



@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoList(request.POST)
        if form.is_valid():
            list_value = form.cleaned_data['list']
            date_value = form.cleaned_data['date']
            mytodo = ListItem(list=list_value, date=date_value)
            mytodo.save()
    else:
        form = TodoList()
    
    return render(request, 'todo.html', {'form': form})

from django.shortcuts import render, redirect
from .models import ListItem


def save_todo(request):
    if request.method == 'POST':
        list_value = request.POST.get('list')
        date_value = request.POST.get('date')
        if list_value:
            mytodo = ListItem(list=list_value, date=date_value)
            mytodo.save()
    
    return redirect('todo')



@login_required
def viewlist(request):
    return render(request, 'view-list.html')


def logout(request):
    auth_logout(request)
    return redirect('login')