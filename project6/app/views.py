from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *

# Create your views here.

def loginp(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if trainer.objects.filter(user_id=user).exists():
            login(request,user)
            return redirect('trainer_homepage')
        elif userr.objects.filter(user_id=user).exists():
            login(request,user)
            return redirect('user_homepage')
        elif admin.objects.filter(user_id=user).exists():
            login(request,user)
            return redirect('admin_homepage')
    else:
        return render(request,'login.html')
# home page
def indexp(request):
    return render(request,'index.html')

# admin_homepage
def adminhp(request):
    return render(request,'admin_homepage.html')

# admin_viewuserbooking
def viewbook(request):
    data = dive.objects.all()
    data1=trainer.objects.all()
    return render(request,'admin_viewuserbooking.html',{'a':data,'b':data1})

def asigntr(request,id):
    if request.method == 'POST':
        trainer_id = request.POST['trainer']
        trainers = trainer.objects.get(id=trainer_id)
        data=dive.objects.get(id=id)
        data.status = "Trainer assigned"
        data.trainer_id=trainers
        data.save()
        return redirect('admin_viewuserbooking')


def completed(request,id):
    data=dive.objects.get(id=id)
    data.status = "Completed"
    data.save()
    return redirect('admin_viewuserbooking')

# admin_viewusers
def viewuser(request):
    data = userr.objects.all()
    return render(request,'admin_viewuser.html',{'a':data})




# user_registration
def userreg(request):
    if request.method == 'POST':
        name = request.POST['Name']
        gender = request.POST['Gender']
        contact = request.POST['Contact']
        email = request.POST['Email']
        password = request.POST['password']
        data = User.objects.create_user(first_name=name,email=email,username=email,password=password)
        data.save()
        data2 = userr.objects.create(name=name,gender=gender,contact=contact,email=email,password=password,user_id=data)
        data2.save()
        
        return HttpResponse('data submitted successfully')
    else:
        return render(request,'user_registration.html')

# user_homepage
def userhp(request):
    data=category.objects.all()
    data1=place.objects.all()
    return render(request,'user_homepage.html',{'a':data,'b':data1})

# user view bookings    
def userviewbook(request):
    data=dive.objects.filter(user_id=request.user.id , status='pending')
    data1=dive.objects.filter(user_id=request.user.id , status='Completed')

    return render(request,'user_viewbookings.html',{'a':data,'b':data1})


# user view profile
def profile(request):
    data=userr.objects.get(user_id=request.user.id)
    return render(request,'user_viewprofile.html',{'i':data})


# trainer_registration
def trainerreg(request):
    if request.method == 'POST':
        name = request.POST['Name']
        gender = request.POST['gender']
        contact = request.POST['contact']
        email = request.POST['Email']
        password = request.POST['password']
        data = User.objects.create_user(first_name=name,email=email,username=email,password=password)
        data.save()
        data1 = trainer.objects.create(name=name,contact=contact,gender=gender,user_id=data,email=email,password=password)
        data1.save()

        return HttpResponse('data submitted successfully')
    else:
        b=trainer.objects.all()
        return render(request,'trainer_registration.html',{'a':b})

# trainer_homepage
def trainerhp(request):
    return render(request,'trainer_homepage.html')

# trainer view bookings
def trainerviewbook(request):
    tr = trainer.objects.get(user_id=request.user)   # find trainer linked to user
    data = dive.objects.filter(trainer_id=tr)     # fetch trainer's dives
    return render(request, 'trainer_viewbookings.html', {'a': data})

def completedbytrainer(request,id):
    data=dive.objects.get(id=id)
    data.status = "Completed"
    data.save()
    return redirect('trainer_viewbookings')

# trainer view profile
# def profile(request):
    data=trainer.objects.get(user_id=request.user.id)
    return render(request,'trainer_viewprofile.html',{'i':data})

# place_add
def addplace(request):
    if request.method == 'POST':
        name = request.POST['Name']
        data = place.objects.create(name=name)
        data.save()
        return HttpResponse('data submitted successfully')
    else:
        b = place.objects.all()
        return render(request,'place_add.html',{'a':b})

# place_delete    
def placedelete(request,id):
    places = place.objects.get(id=id)
    places.delete()
    return redirect('place_add')


# category_add
def addcategory(request):
    if request.method == 'POST':
        name = request.POST['Name']
        description = request.POST['Description']
        data = category.objects.create(name=name,description=description)
        data.save()
        return HttpResponse('data submitted successfully')
    else:
        b = category.objects.all()
        return render(request,'category_add.html',{'a':b})

# category_delete
def categorydelete(request,id):
    categorys = category.objects.get(id=id)
    categorys.delete()
    return redirect('category_add')


# dive_booking
def divebook(request):
    if request.method == 'POST':
        id=User.objects.get(id=request.user.id)
        date = request.POST['Date']
        places_id = request.POST['Location']
        categorys_id = request.POST['category']
        places=place.objects.get(id=places_id)
        categorys=category.objects.get(id=categorys_id)

        data = dive.objects.create(user_id=id,date=date,places=places,categorys=categorys)
        data.save()
        return redirect('user_viewbookings')
    else:
        b = dive.objects.all()
        return render(request,'user_homepage.html',{'a':b})
    

def submit_medical(request, booking_id):
    # get booking
    booking = get_object_or_404(dive, pk=booking_id)

    if request.method == "POST":

        # handling multiple checkboxes
        selected_conditions = request.POST.getlist("conditions")
        conditions_csv = ",".join(selected_conditions)

        # create medical entry
        medical = DiveMedical.objects.create(
            booking=booking,
            full_name=request.POST.get("full_name"),
            dob=request.POST.get("dob"),
            experience_level=request.POST.get("experience_level"),

            emergency_name=request.POST.get("emergency_name"),
            emergency_phone=request.POST.get("emergency_phone"),

            conditions=conditions_csv,
            medical_details=request.POST.get("medical_details"),

            physician=request.POST.get("physician", ""),
            recent_dive=request.POST.get("recent_dive"),
        )

        return redirect("medical_details", pk=medical.pk)

    return render(request, "fun_dive_medical_form.html", {"booking": booking})


def medical_details(request, pk):
    details = get_object_or_404(DiveMedical, pk=pk)
    return render(request, "fun_dive_medical_details.html", {"details": details})

def button_detail(request, id):
    data=dive.objects.get(id=id)
    count=data.count
    buttons = range(1, count + 1)

    return render(request, "admin_button.html", {"buttons": buttons})


