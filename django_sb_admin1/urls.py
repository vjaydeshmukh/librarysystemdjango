from django.urls import path,include
import django_sb_admin1.views
from django.views.generic import TemplateView
# from django.urls import path,include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django_sb_admin1 import views
from django.conf.urls.static import static



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

  path('home',django_sb_admin1.views.home, name='home'),
    # path('login', django_sb_admin1.views.login, name='login'),

   path('s', django_sb_admin1.views.start, name='sb_admin_start'),
    # path('register/', TemplateView.as_view(
    #     template_name="django_sb_admin/register.html"),
    #     name='sb_admin_register'
    # ),
   
    path('forgot_passwordd', TemplateView.as_view(
        template_name="django_sb_admin/forgot_password.html"),
        name='sb_admin_forgot_password'
    ),
    path('404', TemplateView.as_view(
        template_name="django_sb_admin/reg.html"),
        name='sb_admin_404'
    ),
     path('profile', TemplateView.as_view(
        template_name="django_sb_admin/index.html"),
        name='profile'
    ),
    path('add', django_sb_admin1.views.add,name='sb_admin_add'),
        path('books', django_sb_admin1.views.books,name='sb_admin_books'),
   path('issue', django_sb_admin1.views.issue, name='sb_admin_issue'),

   path('register', django_sb_admin1.views.register, name='sb_admin_register'),
  path('user_register', django_sb_admin1.views.user_register, name='user_register'),

   path('loginn', django_sb_admin1.views.login, name='sb_admin_login'),
   path('loginnn/', views.Login.as_view(), name='loginnnn'),

   path('accounts/logout', django_sb_admin1.views.logout, name='sb_admin_logout'),
   path('',django_sb_admin1.views.dashboard, name='sb_admin_dashboard'),
   path('charts', django_sb_admin1.views.charts, name='sb_admin_charts'),
   path('tables', django_sb_admin1.views.tables, name='sb_admin_tables'),
    path('approve', django_sb_admin1.views.approve, name='approve_registration'),
   path('forms', django_sb_admin1.views.forms, name='sb_admin_forms'),
   path('bootstrap-elements', django_sb_admin1.views.bootstrap_elements, name='sb_admin_bootstrap_elements'),
   path('bootstrap-grid', django_sb_admin1.views.bootstrap_grid, name='sb_admin_bootstrap_grid'),
   path('rtl-dashboard', django_sb_admin1.views.rtl_dashboard, name='sb_admin_rtl_dashboard'),
   path('blank', django_sb_admin1.views.admin_add_student_view, name='sb_admin_blank'),
path('delete-student/<int:pk>', django_sb_admin1.views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', django_sb_admin1.views.update_student_view,name='update-student'),

 path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logouttt/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logouttt'),
    # path('password-reset/',auth_views.PasswordResetView.as_view(template_name='django_sb_admin/users/password_reset.html'),name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='users/password_reset_done.html'
    #      ),
    #      name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='users/password_reset_confirm.html'
    #      ),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='users/password_reset_complete.html'
    #      ),
    #      name='password_reset_complete'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)