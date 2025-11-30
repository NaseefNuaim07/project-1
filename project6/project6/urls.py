"""
URL configuration for project6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.indexp,name='index'),
    path('login',views.loginp,name='login'),

    path('admin_homepage',views.adminhp,name='admin_homepage'),
    path('admin_viewuserbooking',views.viewbook,name='admin_viewuserbooking'),
    path('admin_viewuser',views.viewuser,name='admin_viewuser'),
    path('complete/<int:id>',views.completed,name='task_complete'),
    path('astr/<int:id>',views.asigntr,name='assign_trainer'),


    path('user_registration',views.userreg,name='user_registration'),
    path('user_homepage',views.userhp,name='user_homepage'),
    path('user_viewbookings',views.userviewbook,name='user_viewbookings'),
    path('user_viewprofile',views.profile,name='user_viewprofile'),
    path('divebook',views.divebook,name='dive_book'),

    path('trainer_registration',views.trainerreg,name='trainer_registration'),
    path('trainer_homepage',views.trainerhp,name='trainer_homepage'),
    path('trainer_viewbookings',views.trainerviewbook,name='trainer_viewbookings'),
    path('trainer_complete/<int:id>',views.completedbytrainer,name='completed'),
    path('trainer_viewprofile',views.profile,name='trainer_viewprofile'),


    path('place_add',views.addplace,name='place_add'),
    path('placedelete/<int:id>/',views.placedelete,name='placedelete'),

    path('category_add',views.addcategory,name='category_add'),
    path('categorydelete/<int:id>/',views.categorydelete,name='categorydelete'),

    path("medical/<int:booking_id>/fill/", views.submit_medical, name="submit_medical"),
    path("medical/details/<int:pk>/", views.medical_details, name="medical_details"),

    path("button/<int:id>/", views.button_detail, name="button_detail"),



    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)