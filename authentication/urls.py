"""authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from authapp.views import signin, signup, signout,reset,BookReadView,contact,Books
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django_sb_admin1.views import dashboard
app_name = 'authentication'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('f', views.home, name='home'),
    path('sangam/', include('django.contrib.auth.urls')),
    # path('signup/', views.signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    # path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('<int:book_id>/', views.DetailView.as_view(), name='detail'),

    path('accounts/', include('allauth.urls')),
    path('i', views.index.as_view(), name='index'),
    path('',  include('django_sb_admin1.urls')),
   # path('j/', dashboard, name='dashboard'),
 path('about/', TemplateView.as_view(
        template_name="about.html"),
        name='about'
    ),
  path('contact/', contact, name='contact'),
    path('Books/', Books.as_view(), name='Books'),

    # path('contact/' ,views.contact,name='contactPage'),
         
    #      path('contacts/' ,views.contacts,name='contactPage'),

         # path('about/' ,views.about,name='about_page'),
             path('read/<int:pk>', BookReadView.as_view(), name='read_book'),

         path('signup/' ,views.handleSignup,name='handleSignup'),
         
         path('login/' ,views.handleLogin,name='handleLogin'),

         path('logout/' ,views.handleLogout,name='handleLogout'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

