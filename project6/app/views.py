from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def loginp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_superuser==False:
            login(request,user)
            return redirect('user_home')
        else:
            return render(request,'login.html',{'error':'invalid username or password'})
    else:
        return render(request,'login.html')

def indexp(request):
    return render(request,'index.html')

def adminhp(request):
    return render(request,'admin_homepage.html')






def userreg(request):
    if request.method == 'POST':
        name = request.POST['Name']
        gender = request.POST['Gender']
        mobile = request.POST['Mobile']
        email = request.POST['Email']
        password = request.POST['password']
        data=User.objects.create_user(name=name,gender=gender,mobile=mobile,email=email,password=password)
        data.save()
        return HttpResponse('data submitted successfully')
    else:
        return render(request,'user_registration.html')
    
def userhp(request):
    return render(request,'user_homepage.html')
def userviewbook(request):
    return render(request,'user_viewbookings.html')






def trainerhp(request):
    return render(request,'trainer_homepage.html')
def trainerviewbook(request):
    return render(request,'trainer_viewbookings.html')






def uview(request):
    return render(request,'uview.html')