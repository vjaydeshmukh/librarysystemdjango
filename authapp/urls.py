from django.urls import path
from . import views

urlpatterns = [
    path('reset/', reset, name='reset'),
    path('accounts/', include('allauth.urls'))
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
 path('signup/' ,views.handleSignup,name='handleSignup'),
         
         path('login/' ,views.handleLogin,name='handleLogin'),

         path('logout/' ,views.handleLogout,name='handleLogout'),

]