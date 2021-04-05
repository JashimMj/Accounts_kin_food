"""software URL Configuration

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

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index,name='index'),
    path('', views.maindashboard,name='dashboard'),
    path('adminDashboard', views.adminD,name='adminDashboard'),
    path('accounts/', views.accountD, name='accounts'),
                #########################
                ## Company Information ##
                #########################
    path('companyinfo/', views.companyinfoV,name='companyinfo'),
    path('companyinfo/save/', views.companyinfosaveV,name='companyinfosave'),
    path('companyinfo/edit/<int:id>/', views.companyinfoeditV,name='companyinfoedit'),
    path('companyinfo/update/', views.companyinfoupdateV,name='companyinfoupdate'),
    path('companyinfo/delete/<int:id>', views.companyinfodeleteV,name='companyinfodelete'),
                #########################
                ## Client Information  ##
                #########################
    path('Client/information/', views.ClientinfoV,name='clientinfo'),
    path('Client/information/save/', views.ClientinfosaveV,name='clientinfosave'),
    path('Client/information/edit/<int:id>', views.ClientinfoeditV,name='clientinfoedit'),
    path('Client/information/update/', views.ClientinfoupdateV,name='clientinfoupdate'),
    path('Client/information/delete/<int:id>', views.ClientinfodeleteV,name='clientinfodelete'),
                #########################
                # producer Information #
                #########################
    path('Producer/information/', views.ProducerinfoV,name='Producerinfo'),
    path('Producer/information/save/', views.ProducerinfosaveV,name='Producerinfosave'),
    path('Producer/information/edit/<int:id>', views.ProducerinfoeditV,name='Producerinfoedit'),
    path('Producer/information/update/', views.ProducerinfoupdateV,name='Producerinfoupdate'),
    path('Producer/information/delete/<int:id>', views.ProducerinfodeleteV,name='Producerinfodelete'),

                  #########################
                  ##  Entry Information  ##
                  #########################
    path('Entry/', views.EntryV,name='Entry'),
    path('Entry/save/', views.EntrysaveV,name='Entrysave'),
    path('Entry/edit/<int:id>/', views.EntryeditV,name='Entryedit'),
    path('Entry/Update/', views.EntryupdateV,name='Entryupdate'),
    path('Entry/Delete/<int:id>', views.entrydeleteV,name='Entrydelete'),

                  #########################
                  ##PDF Client Information##
                  #########################

    path('Client/Report/', views.client_wiseV, name='Crep'),
    path('ClientWise/Report/', views.CreportV, name='Creport'),


                   #########################
                  ##PDF Client Information##
                  #########################
    path('Producer/Report/', views.Producer_wiseV, name='prep'),
    path('Producers/', views.preportV, name='preport'),

                   #########################
                  ##Collection Information##
                  #########################
    path('Collection/Report/', views.CollectionReportV, name='CollectionReport'),
    path('Collections/', views.collectionV, name='Collection'),
                #########################
                  ##Dues Information##
                  #########################
    path('Dues/Report/', views.DuesReportV, name='DuesReport'),
    path('Due/', views.DuesV, name='Dues'),


    path('Loging/', views.LogingV, name='Loging'),
    path('Logout/', views.logoutV, name='logout'),
    path('Singup/', views.SingupV, name='Singup'),



    path('part/payment/', views.partpayment, name='partpayment'),
    path('part/payment/save/', views.paymentsave, name='partpaymentsave'),



























]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
