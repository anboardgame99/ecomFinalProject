from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect

from userauths.models import User

def resgister_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You're already logged in.")
        return redirect("home:index")

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
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


# def login_view(request):
#     if request.user.is_authenticated:
#         messages.warning(request, f"You're already logged in.")
#         return redirect("home:index")
#
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#
#         try:
#             user = User.object.get(email=email)
#         except:
#             messages.warning(request, f"User with {email} does not exist")
#
#         user = authenticate(request, email=email, password=password)
#
#         if user is not None:
#             login(request, user)
#             messages.success(request, "You are logged in.")
#             return redirect("home:index")
#         else:
#             messages.warning(request, "User does not exist. Create an account.")
#
#     context = {
#
#     }
#
#     return render(request, "userauths/login.html", context)
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You're already logged in.")
        return redirect("home:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, "User does not exist.")
            return redirect("userauths:login")

        if 'login_admin' in request.POST:  # Check if "Login with Admin" button is clicked
            if user.is_staff:
                admin = authenticate(request, email=email, password=password)
                if admin is not None:
                    login(request, admin)
                    messages.success(request, "You are logged in as an admin.")
                    return redirect("admin:index")  # Redirect to the admin dashboard upon successful login
                else:
                    messages.warning(request, "Invalid admin credentials.")
                    return redirect("userauths:login")
            else:
                messages.warning(request, "You are not authorized to log in as an admin.")
                return redirect("userauths:login")

        elif 'login_user' in request.POST:  # Check if "Login" button is clicked
            if not user.is_staff:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You are logged in.")
                    return redirect("home:index")  # Redirect to the user dashboard upon successful login
                else:
                    messages.warning(request, "Invalid user credentials.")
                    return redirect("userauths:login")
            else:
                messages.warning(request, "Admin users cannot log in as regular users.")
                return redirect("userauths:login")

    return render(request, "userauths/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("home:index")

