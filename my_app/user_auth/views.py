from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, LoginForm, RegisterForm

def registration(request):
    """
    View to handle user registration.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Redirects to 'polls:index' on successful registration,
      or renders the registration form on GET request with errors if any.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    elif request.method == 'GET':
        form = RegisterForm()

    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        firstname = form.cleaned_data['first_name']
        user = authenticate(username=username, password=password, first_name=firstname)
        login(request, user)
        return redirect('polls:index')

    return render(request, 'registration/register_user.html', {'form': form})

def user_login(request):
    """
    View to handle user login.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Redirects to 'polls:index' on successful login,
      or renders the login form on GET request with errors if any.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
    elif request.method == 'GET':
        form = LoginForm(request.GET)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            form = UserCreationForm()

    return render(request, 'registration/login_user.html', {'form': form})


