import functools
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import User

# Create your views here.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(request, *args, **kwargs):
        if 'userid' not in request.session:
            return HttpResponseRedirect(reverse('djfauth:login'))
        return view(request, *args, **kwargs)
    return wrapped_view
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                pass
            else:
                error = 'User {} is already registered.'.format(username)

        if error is None:
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect(reverse('djfauth:login'))

        messages.add_message(request, messages.INFO, error)
    if 'userid' in request.session:
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'djfauth/register.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        error = None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            error = 'Incorrect username.'
        else:
            if not user.check_password_hash(password):
               error = 'Incorrect password.'
        
        if error is None:
            request.session['userid'] = user.id
            request.session.set_expiry(300)
            return HttpResponseRedirect(reverse('home'))

        messages.add_message(request, messages.INFO, error)
        
    if 'userid' in request.session:
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'djfauth/login.html')

def logout(request):
    try:
        del request.session['userid']
    except KeyError:
        pass
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))