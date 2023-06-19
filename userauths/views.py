from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect


# from userauths.models import User

# from django.conf import settings

# User = settings.AUTH_USER_MODEL
# Create your views here.
def resgister_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You're already logged in.")
        return redirect("home:index")

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            # new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")

            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)

            return redirect("home:index")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You're already logged in.")
        return redirect("home:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if 'login' in request.POST:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in.")
                return redirect("home:index")
            else:
                messages.warning(request, "Invalid credentials.")
        elif 'admin' in request.POST:
            email = request.POST.get("email")
            user = authenticate(request, username=email, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, "Admin login successful.")
                return redirect("admin:index")
            else:
                messages.warning(request, "Admin login failed.")

    return render(request, "userauths/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("home:index")
