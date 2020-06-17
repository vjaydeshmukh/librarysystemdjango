from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import LoginForm, RegistrationForm,ResetForm ,ContactusForm     
from .models import Destination
from django.views import View
from django.core.paginator import Paginator


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from validate_email import validate_email
from django.core.mail import send_mail
from authentication.settings import EMAIL_HOST_USER


from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings



from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

# from .forms import BookForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Book


class Index(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'


# class BookCreateView(BSModalCreateView):
#     template_name = 'examples/create_book.html'
#     form_class = BookForm
#     success_message = 'Success: Book was created.'
#     success_url = reverse_lazy('index')


# class BookUpdateView(BSModalUpdateView):
#     model = Book
#     template_name = 'examples/update_book.html'
#     form_class = BookForm
#     success_message = 'Success: Book was updated.'
#     success_url = reverse_lazy('index')

def contact(request):
    sub = ContactusForm()
    print(sub)
    if request.method == 'POST':
        sub = ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['gcoej4@gmail.com'], fail_silently = False)
            return render(request, 'contactsuccess.html')
    return render(request, 'contact.html', {'form':sub})



class Books(View):
    last_login_cookie = 'last_login'
    def get(self,request):
        
        paginate_by = 3
        last_login = ''
        if self.last_login_cookie in request.session.keys():
            userlogin = request.session.get(self.last_login_cookie)
        else:
            userlogin = 'Your last login was more than one hour ago'
            print(userlogin)
        distt = Destination.objects.all().order_by('id')[:20]
        paginator = Paginator(distt, 4)
        page = request.GET.get('page')
        print(page)
        distt = paginator.get_page(page)
        print(distt)
        allProds=[distt]
        return render(request, 'main/book_card.html',{ "allProds": allProds,"userlogin":userlogin })
    # catProds=Destination.objects.values('category','id')





class BookReadView(BSModalReadView):
    print("hii")
    model = Destination
    template_name = 'read_book.html'


# class BookDeleteView(BSModalDeleteView):
#     model = Book
#     template_name = 'examples/delete_book.html'
#     success_message = 'Success: Book was deleted.'
#     success_url = reverse_lazy('index')


# class SignUpView(BSModalCreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'examples/signup.html'
#     success_message = 'Success: Sign up succeeded. You can now Log in.'
#     success_url = reverse_lazy('index')


# class CustomLoginView(BSModalLoginView):
#     authentication_form = CustomAuthenticationForm
#     template_name = 'examples/login.html'
#     success_message = 'Success: You were successfully logged in.'
#     success_url = reverse_lazy('index')










def home(request):
    paginate_by = 3
    distt = Destination.objects.all()
    print(distt)
    allProds=[]
    catProds=Destination.objects.values('category','id')
    print(catProds)
    cats={item['category'] for item in catProds}
    print(len(cats))
    print(cats)
    for cat in cats:
        prod=Destination.objects.filter(category=cat)
        print(prod)
        allProds.append([prod])

    
    return render(request, 'index.html',{ "allProds": allProds })



def about(request):
    return render(request,'signin.html')
# class RegistrationView(View):
#     def get(self,request):
#         return render(request,'auth/register.html')


#     def post(self,request):
#         context={
            
#             'data':request.POST,
#             'has_error':False
#             }



#         email=request.POST.get('email')
#         username=request.POST.get('username')
#         full_name=request.POST.get('name')
#         password=request.POST.get('password')
#         password2=request.POST.get('password2')

#         if len(password)<6:
#              messages.add_message(request,messages.ERROR,'passwords should be atleast 6 characters long')
#              context['has_error']=True
#         if password!=password2:
#              messages.add_message(request,messages.ERROR,'passwords dont match')
#              context['has_error']=True
        
#         if not validate_email(email):
#             messages.add_message(request,messages.ERROR,'Please provide a valid email')
#             context['has_error']=True

#         try:
#             if User.objects.get(email=email):
#                 messages.add_message(request,messages.ERROR,'Email is taken')
#                 context['has_error']=True
                
#         except Exception as identifier:
#             pass

#         try:
#             if User.objects.get(username=username):
#                 messages.add_message(request,messages.ERROR,'Username is taken')
#                 context['has_error']=True
                
#         except Exception as identifier:
#             pass

#         if context['has_error']:
#             return render(request,'auth/register.html',context,status=400)

#         user=User.objects.create_user(username=username,email=email)
#         user.set_password(password)
#         user.first_name=full_name
#         user.last_name=full_name
#         user.is_active=False
#         user.save()

#         current_site=get_current_site(request)
#         email_subject='Active your Account'
#         message=render_to_string('auth/activate.html',
#         {
#             'user':user,
#             'domain':current_site.domain,
#             'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#             'token':generate_token.make_token(user)
#         }
#         )

#         email_message = EmailMessage(
#         email_subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [email]
#         )

#         email_message.send()

#         messages.add_message(request,messages.SUCCESS,'account created succesfully')

#         return redirect('login')



        

# class LoginView(View):
#     def get(self,request):
#         return render(request,'auth/login.html')
#     def post(self,request):
#         context={
#             'data':request.POST,
#             'has_error':False
#         }
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         if username=='':
#             messages.add_message(request,messages.ERROR,'Username is required')
#             context['has_error']=True
#         if password=='':
#             messages.add_message(request,messages.ERROR,'Password is required')
#             context['has_error']=True
        
#         user=authenticate(request,username=username,password=password)

#         if not user and not context['has_error']:
#              messages.add_message(request,messages.ERROR,'Invalid login')
#              context['has_error']=True
        
#         if context['has_error']:
#              return render(request,'auth/login.html',status=401,context=context)
#         login(request,user)
#         return redirect('home')

        
        

# class ActivateAccountView(View):
#     def get(self,request,uidb64,token):
#         try:
#             uid=force_text(urlsafe_base64_decode(uidb64))
#             user=User.objects.get(pk=uid)
#         except Exception as identifier:
#             user=None

#         if user is not None and generate_token.check_token(user,token):
#             user.is_active=True
#             user.save()
#             messages.add_message(request,messages.SUCCESS,'account activated sucesfully')
#             return redirect('login')
#         return render(request,'auth/activate_failed.html',status=401)


# class HomeView(View):
#     def get(self,request):
#         return render(request,'home.html')

# class LogoutView(View):
#     def post(self,request):
#         logout(request)
#         messages.add_message(request,messages.SUCCESS,'Logout successfully')
#         return redirect('login')







# import pyrebase
# from .forms import SignupForm
# def signup(request):

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = SignupForm() #just get request of form
#     return render(request, 'signup.html', {
#         'form': form
#     })




def signin(request):
    forms = LoginForm()
    # messages.add_message(request,messages.SUCCESS,'Login Required')
    if request.method == 'POST':
        # context={
        #     'has_error':False
        # }
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)

            # if not user and not context['has_error']:
            #     messages.add_message(request,messages.ERROR,'Invalid login')
            #     context['has_error']=True
        
            # if context['has_error']:
            #     return render(request,'signin.html',status=401,context=context)
            # login(request,user)
            # return redirect('home')


            if user:
                login(request, user)
                messages.success(request, "successfuly logged in ")
                return redirect('index')
            else :
                context = {
        'form': forms,
        'error': 'This Username & Password Wrong!',
                }
                return render(request, 'signin.html', context)                
    context = {
        'form': forms,
    }
    return render(request, 'signin.html', context)

def reset(request):
    forms = ResetForm()
    if request.method == 'POST':
        forms = ResetForm(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data['email']
            email_qs = User.objects.filter(email=email)
            print("email matched")
            
            if email_qs:
                print("email matched")
                context = {
        'form': forms,
        'success':'Reset Link is emailed you ! '}
                return render(request, 'reset.html', context)
            else :
                context = {
        'form': forms,
        'error': 'This email Not exists!'}
                return render(request, 'reset.html', context)


    context = {
        'form': forms,
    }
    return render(request, 'reset.html', context)




# def reset(request):
#     forms = ResetForm()
#     if request.method == 'POST':
#         forms = ResetForm(request.POST)
#         if forms.is_valid():
#             email = forms.cleaned_data['email']
    
#         return redirect('home')
#     context = {
#         'form': forms
#     }
#     return render(request, 'reset.html', context)





def signup(request):

    forms = RegistrationForm()
    if request.method == 'POST':
        # context={
            
        #     # 'data':request.POST,
        #     'has_error':False
        #     }
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']

            # if len(password)<6:
            #     messages.add_message(request,messages.ERROR,'passwords should be atleast 6 characters long')
            #     context['has_error']=True
            # if password!=password2:
            #     messages.add_message(request,messages.ERROR,'passwords dont match')
            #     context['has_error']=True



            # if context['has_error']:
            #     return render(request,'register.html',context,status=400)

            # user=User.objects.create_user(username=username,email=email)
            # user.set_password(password)
            # user.first_name=full_name
            # user.last_name=full_name
            # user.is_active=False
            # user.save()

            # current_site=get_current_site(request)
            # email_subject='Active your Account'
            # message=render_to_string('activate.html',
            # {
            #     'user':user,
            #     'domain':current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':generate_token.make_token(user)
            # }
            # )

            # email_message = EmailMessage(
            # email_subject,
            # message,
            # settings.EMAIL_HOST_USER,
            # [email]
            # )

            # email_message.send()

            # messages.add_message(request,messages.SUCCESS,'account created succesfully')

            # return redirect('signin')




            if password == confirm_password and not User.objects.filter(email=email):
                try:
                    user=User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    print("created")
                    user.is_active=False
                    print(user.is_active)
                    user.save()
                    print("user saved")

                    current_site=get_current_site(request)
                    email_subject='Active your Account'
                    print(email_subject)
                    message=render_to_string('activate.html',
                    {
                        'user':user,
                        'domain':current_site.domain,
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'token':generate_token.make_token(user)
                    }
                    )

                    email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email]
                    )
                    email_message.send()
                    print(email_message)
                    # messages.add_message(request,messages.SUCCESS,'account created succesfully')
                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!',
                        }
                    return render(request, 'signup.html', context)

            context = {
        'form': forms,
        'emailerror': 'This Email Already exists!'
            }
            return render(request, 'signup.html', context)

    context = {
        'form': forms,
    }
    return render(request, 'signup.html', context)

def signout(request):
    logout(request)
    return redirect('index')




class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None

        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.add_message(request,messages.SUCCESS,'account activated sucesfully')
            return redirect('signin')
        return render(request,'activate_failed.html',status=401)











