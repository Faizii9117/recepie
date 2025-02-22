from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

# def index(request):
#     students = [
#         {'name': 'faisal','age':'21'},
#         {'name':'farhan','age':'22'},
#         {'name':'anas','age':'17'},
#         {'name':'nabeel','age':'14'},
#         {'name':'uzair','age':'18'},
#     ]
#     return render (request, "index.html", context={'school':students})
    
def recepie(request):
    if request.user.is_anonymous:
        return redirect("/login")
    

    if request.method == "POST":
        data=request.POST
        recepie_name=data.get("recepie_name")  
        recepie_desc=data.get('recepie_desc') 
        recepie_image=request.FILES.get('recepie_image')

        vegi.objects.create(
          recepie_name=recepie_name,
          recepie_desc=recepie_desc,
          recepie_image=recepie_image
        )
        return redirect("/recepie ")
    data = vegi.objects.all()
    context={'recepie_data':data}

    return render (request , 'recepie.html',context)




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)  # ✅ Authenticate using Django User model

        if user is not None:
            auth_login(request, user)  # ✅ Correct login function
            messages.success(request, "Login successful!")
            return redirect("recepie")  # Redirect to your recipe page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")



def delete_recepie(request,id):
    queryset=vegi.objects.get(id=id)
    queryset.delete()
    return redirect('/recepie/')



from django.contrib.auth.hashers import make_password, check_password

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "").strip()
        password2 = request.POST.get("password2", "").strip()

        if not username or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # ✅ Correct way to create a user
        user = User.objects.create_user(username=username, password=password1)

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "register.html")



def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

