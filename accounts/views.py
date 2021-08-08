from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['Password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are logged in")
            return redirect('dashboard')
        else:
            messages.error(request,"invalid login")
            return render(request,'login.html')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        firstname =request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exit')
                return redirect('lregister')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exit')
                    return redirect('lregister')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    auth.login(request,user)
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,"registered sucess")
                    return redirect('login')





        else:
            messages.error(request,'password not match')


    else:
        return render(request,"register.html")

    return render(request,"register.html")

def dashboard(request):
    return render(request,"dashboard.html")

def logout(request):
    if request.method =='POST':
        auth.logout(request)

        return redirect('home')
    return redirect( "home")
