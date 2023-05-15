from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import Account_applicationForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged successfully')
            return redirect('home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        cpassword = request.POST['pass2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                messages.success(request, 'Signup successfully')
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    return render(request, 'register.html')


def msg(request):
    return render(request, 'message.html')


def home(request):
    return render(request, 'home.html')


def accountapplication(request):
    ds = District.objects.all()
    br = Branches.objects.all()
    return render(request, "account_application.html", {'dis': ds, 'b': br})


def account_application(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        print(district)
        dis = District.objects.get(Dist_name=district)
        branch = request.POST['branch']
        print(branch)
        brnch = Branches.objects.get(sub_name=branch)
        # print("branchname:", brnch)
        application = Account_application.objects.create(firstname=firstname, dob=dob, age=age, gender=gender,
                                                         phn=phone,
                                                         email=email, address=address, district=dis, branch=brnch)
        application.save()
        messages.success(request, 'Application submitted successfully')
        return redirect('msg')
    return render(request, 'account_application.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
