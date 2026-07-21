from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('registerUser/', views.registerUser, name = 'registerUser'),

    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('myAccount/', views.myAccount, name = 'myAccount'),
    path('customerDashboard/', views.custDashboard, name = 'customerDashboard'),
    path('vendorDashboard/', views.vendorDashboard, name = 'vendorDashboard'),
   
]
