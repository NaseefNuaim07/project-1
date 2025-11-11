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

    path('user_registration',views.userreg,name='user_registration'),
    path('user_homepage',views.userhp,name='user_homepage'),
    path('user_viewbookings',views.userviewbook,name='user_viewbookings'),

    path('trainer_registration',views.trainerreg,name='trainer_registration'),
    path('trainer_homepage',views.trainerhp,name='trainer_homepage'),
    path('trainer_viewbookings',views.trainerviewbook,name='trainer_viewbookings'),



    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)