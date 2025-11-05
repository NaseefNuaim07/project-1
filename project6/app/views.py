from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.

def loginp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_superuser==False:
            login(request,user)
            return redirect('userhome')
        else:
            return render(request,'login.html',{'error':'invalid username or password'})
    else:
        return render(request,'login.html')

def indexp(request):
    return render(request,'index.html')

