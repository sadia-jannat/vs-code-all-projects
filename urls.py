"""finaldjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
#from .import views


#image add ar jonno
from django.conf import settings
from django.conf.urls.static import static

from final import views

#API
from final.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
   
    #bellow path not related our main path
    path('homepage/',views.home), 

    path('',views.indexpage, name='indexpage'),
    path('userform/',views.userform),

    path('test/',views.test),

    path('delete/<int:id>/', views.delete_data, name="deletedata"),

    path('<int:id>/', views.update_data, name="updatedata"),



    #house final ar page start
    path('house/', views.house, name='house'),
    path('houseform/', views.houseform, name='houseform'),
    path('rental/', views.rental, name='rental'),
    path('owner/', views.owner, name='owner'),
    path('search/', views.search, name='search'),   #try for fetch rate
    

    #this signin and login for django UserCreationForm their site use
    path('signup/', views.signup, name='signup'),
    path('uselog/', views.uselog, name='uselog'),

    
    #ownerform page for house details add by house owner that will go to database
    path('ownerform/', views.ownerform, name='ownerform'),

    path('fill/', views.fill, name='fill'),
    path('imgall/', views.imgall, name='imgall'),
    path('dhaka/', views.dhaka, name='dhaka'),
    path('info/<str:pk>', views.info, name='info'), #details data primary key(pk) ar maddhome dekhabe
    
    path('tes/', views.tes, name='tes'),
    path('t/<str:pk>', views.t, name='t'),
    path('save/<int:pid>', views.save, name='save'),

 #location 
    path('get-location/', get_location),

   
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
