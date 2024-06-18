from django.shortcuts import render,redirect
from.forms import ProfileForm,LoginForm,UserRegistrationForm
from django.contrib.auth import login,logout,authenticate


def login_user(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("home")
            return redirect("login")
    else:
        form=LoginForm()
    return render(request, "users/login.html",{'form':form})

def register_customer(request):  
    if request.method == "POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_customer=True
            user.save()
            return redirect("login")
        return redirect("register_customer")
    else:
        form=UserRegistrationForm()
    return render(request, "users/register_customer.html",{"form":form})

def register_worker(request):
    if request.method == "POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_worker=True
            user.save()
            return redirect("worker-register-form")
        return redirect("register_worker")
    else:
        form=UserRegistrationForm()
    return render(request, "users/register_worker.html",{"form":form})


def logout_user(request):
        logout(request)
        return redirect("login")

def register_template(request):
    return render(request, "users/register.html")

