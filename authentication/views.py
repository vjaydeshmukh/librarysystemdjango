from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from authapp.models import Destination
from django.views import View

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse



from django.core.paginator import Paginator


# class IndexView(View):
#     template_name = 'myapp/index.html'
#     last_login_cookie = 'last_login'

#     def get(self, request):
#         print("Get method")
#         last_login = ''
#         if self.last_login_cookie in request.session.keys():
#             userlogin = request.session.get(self.last_login_cookie)
#         else:
#             userlogin = 'Your last login was more than one hour ago'
#             print(userlogin)
#         booklist = Book.objects.all().order_by('id')[:20]
#         print(booklist)
#         paginator = Paginator(booklist, 4)
#         page = request.GET.get('page')
#         booklist = paginator.get_page(page)
#         return render(request, self.template_name, {'booklist': booklist, 'userlogin': userlogin})




# @login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')




class index(View):
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
		return render(request, 'index.html',{ "allProds": allProds,"userlogin":userlogin })
    # catProds=Destination.objects.values('category','id')
    # print(catProds)
    # cats={item['category'] for item in catProds}
    # print(len(cats))
    # print(cats)
    # for cat in cats:
    #     prod=Destination.objects.filter(category=cat)
    #     print(prod)
    #     allProds.append([prod])

    
class DetailView(View):
    # template_name = 'detail.html'

    def get(self, request, book_id):
    	print(book_id)
    	book = get_object_or_404(Destination, id=book_id)
    	print(book.name)
    	return HttpResponse(book.name)
    	# return render(request, self.template_name, {'book': book})
        
        
    





def handleSignup(request):
    if request.method == 'POST':
        # get post parameters
        print("post method")
        signupusername = request.POST ['signupusername']
        print(signupusername)
        fname = request.POST ['fname']
        lname = request.POST ['lname']
        signupemail = request.POST ['signupemail']
        signuppassword = request.POST ['signuppassword']
        password1 = request.POST ['password1']
        print(password1)
        # check for errorneous inputs
        if not signupusername.isalnum():
            # print("nott alnum")
            messages.error(request,"username should only contain letters and numbers")
            print("nott alnum")
            return redirect('home')

        
        if len(signupusername) > 15:
            messages.error(request,"username must be under 15 characters")
            return redirect('home')
        
        if signuppassword != password1:
            # print("not matched")
            messages.error(request,"passwords do not match")
            print("not matched")
            return redirect('home')
        if User.objects.filter(username=signupusername).exists() :
            # print("alraeady")
            messages.info(request,"username already in use !")
            return redirect('home')
        else:
            # create the user
            myuser = User.objects.create_user(signupusername, signupemail, signuppassword)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            print("saved")
            myuser2 = authenticate(username=signupusername , password=signuppassword)
            login(request, myuser2)
            # print(myuser.first_name)
            messages.success(request,"Your ICoder account has Successfuly created !")
            params={'messages': "Please make sure to enter relevant search query"}  
            return redirect('home',params)
        
    else:
        return redirect('error')
# this is login page.
def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername , password=loginpassword)
        if user is not None :
            login(request ,user)
            messages.success(request,"successfuly logged in ")
            return redirect('sb_admin_dashboard')
        else:
            messages.error(request,"invalid credentials, please try again later")
            return redirect('index')
    else:
        return redirect('error')

def detail(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername , password=loginpassword)
        if user is not None :
            login(request ,user)
            messages.success(request,"successfuly logged in ")
            return redirect('sb_admin_dashboard')
        else:
            messages.error(request,"invalid credentials, please try again later")
            return redirect('index')
    else:
        return redirect('error')

 # this is for logout 
def handleLogout(request):
    logout(request)
    messages.success(request, "successfuly logged out ")
    return redirect('index')

