from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

class UserProfileView(DetailView):
    model = User
    slug_field = "username"
    template_name = "user_management/user_account.html"


# TODO check if the user is already logged in.
def index(request):
    if request.user.is_authenticated():
        return render(request, "user_management/my_account.html")
    else:
        return render(request, "user_management/my_account.html")
    return render(request, "user_management/index.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'user_management/signup.html', {'form': form})
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

def login(request):
    return HttpResponse("login page")

def logout(request):
    return HttpResponse("logout page")

def user_account(request):
    # return render(HttpResponse("user accout page"))
    return HttpResponse("user accout page.")
