from django.contrib.auth import (
    login,
    logout,
)
from django.shortcuts import (
    render,
    redirect
)
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .backend import EmailBackend
from django.contrib.auth.models import User


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            user = User.objects.create_user(
                password=raw_password,
                email=email,
                username=username,
            )
            user.save()
            return redirect('log_in')
    else:
        form = SignUpForm()
    return render(request, 'user_base/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['password']
        user = EmailBackend().authenticate(
            request,
            username=mail,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("error")
    return render(request, 'user_base/login.html')


@login_required
def logged_out(request):
    logout(request)
    return redirect('/')
