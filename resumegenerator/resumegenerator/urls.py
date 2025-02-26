"""
URL configuration for resumegenerator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from resumedetails.views import details,resume,allusers,deluser,employeedetails,viewresume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', details,name='details'),
    path('<int:id>/', resume,name='resume'),
    path('allusers', allusers,name='allusers'),
    path('deluser/<int:id>', deluser,name="deluser"),
    path('employeedetails', employeedetails,name="employeedetails"),
    path('view/<int:id>', viewresume,name="viewresume")
]
