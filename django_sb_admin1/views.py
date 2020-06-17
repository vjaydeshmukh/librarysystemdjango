from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import TemplateView, View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# from .forms import StudentForm
from django.http import HttpResponse
from django.shortcuts import render , redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib import messages

from os.path import join as isfile
from django.conf import settings
import os
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

#from letsdo.forms import EmployeeForm
from .models import Students
from .models import MemberProfile,User
from .forms import SignupForm,AdminSigupForm,StudentUserForm,StudentExtraForm,StudentUserForm1,StudentExtraForm1
from . import forms,models

def home(request):
    count = User.objects.count()
    print(count)
    return render(request, 'django_sb_admin/users/home.html',{'count': count})




def registerrrr(request):
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']

        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
                user.save();
                messages.info(request,'new user created')
                return redirect('login')
                
        else:
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')




# def admin_signup_view(request):
#     # AdminSignUpForm form is created
#     form=AdminSigupForm()
#     print("i am in admin_signup_view")
#     if request.method=='POST':
#         print("signupform is submitted request.post method succussful")
#         form=forms.AdminSigupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()


#             my_admin_group = Group.objects.get_or_create(name='ADMIN')
#             my_admin_group[0].user_set.add(user)

#             return HttpResponseRedirect('adminlogin')
#     #form is also travelled with it 
#     return render(request,'django_sb_admin/sb_admin_blank.html',{'form':form})

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
def issue(request):
    if request.method == "POST":
        username = request.POST['libid']
        print(username)
        # user = User.objects.filter(username=username).exists()
        if User.objects.filter(username=username).exists():
            print("success")
            messages.success(request,"successfuly logged in ")
            return redirect('sb_admin_404')
        else:
            messages.error(request,"invalid credentials, please try again later")
            return redirect('404')
    else:
        return redirect('sb_admin_404')







def admin_add_student_view(request):
    print("get method redirted to blank.html")
    form1=StudentUserForm1()
    form2=StudentExtraForm1()
    thank=False
    employees = MemberProfile.objects.all()
    # return render(request,"django_sb_admin/sb_admin_blank.html", {'employees': employees})
    mydict={'form1':form1,'form2':form2,'employees': employees}
    if request.method=='POST':
        thank=True
        form1=StudentUserForm1(request.POST)
        form2=StudentExtraForm1(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print("form is invalid")
            thank=True
            messages.info(request,'form is not valid ')
        # return HttpResponseRedirect('blank')
        return redirect('sb_admin_blank')

        # return render(request,'django_sb_admin/sb_admin_blank.html', {'thank': thank})
    return render(request,'django_sb_admin/sb_admin_blank.html',context=mydict)

def delete_student_view(request,pk):
    student=models.MemberProfile.objects.get(id=pk)
    user=models.User.objects.get(id=student.id)
    user.delete()
    student.delete()
    return redirect('sb_admin_blank')

def update_student_view(request,pk):
    thank=False
    student=models.MemberProfile.objects.get(id=pk)
    user=models.User.objects.get(id=student.id)
    form1=StudentUserForm1(instance=user)
    form2=StudentExtraForm1(instance=student)
    employees = MemberProfile.objects.all()
    mydict={'form1':form1,'form2':form2,'employees': employees}
    if request.method=='POST':
        form1=StudentUserForm1(request.POST,instance=user)
        form2=StudentExtraForm1(request.POST,instance=student)
        print(form1)
        thank=True
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            thank=True
            return redirect('sb_admin_blank', {'thank': thank})
    return render(request,'django_sb_admin/sb_admin_blank.html',context=mydict)




def add(request):
    form1=StudentUserForm()
    form2=StudentExtraForm()
    # employees = MemberProfile.objects.all()
    # return render(request,"django_sb_admin/sb_admin_blank.html", {'employees': employees})
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=StudentUserForm(request.POST)
        form2=StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('add')
    return render(request,'django_sb_admin/sb_admin_add.html',context=mydict)


def books(request):
    form1=StudentUserForm()
    form2=StudentExtraForm()
    # employees = MemberProfile.objects.all()
    # return render(request,"django_sb_admin/sb_admin_blank.html", {'employees': employees})
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=StudentUserForm(request.POST)
        form2=StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('add')
    return render(request,'django_sb_admin/books.html',context=mydict)







@login_required
def homee(request):
    """ 
    Shows our dashboard containing number of students, courses, lecturers, repating students, 
    carry over students and 1st class students in an interactive graph

    """
    students = Students.objects.all().count()
    staff = User.objects.filter(is_lecturer=True).count()
    courses = Course.objects.all().count()
    current_semester = Semester.objects.get(is_current_semester=True)
    no_of_1st_class_students = Result.objects.filter(cgpa__gte=4.5).count()
    no_of_carry_over_students = CarryOverStudent.objects.all().count()
    no_of_students_to_repeat = RepeatingStudent.objects.all().count()

    context = {
        "no_of_students": students,
        "no_of_staff":staff,
        "no_of_courses": courses,
        "no_of_1st_class_students": no_of_1st_class_students,
        "no_of_students_to_repeat": no_of_students_to_repeat,
        "no_of_carry_over_students": no_of_carry_over_students,
    }

    return render(request, 'result/home.html', context)








# class StudentCreateView(LoginRequiredMixin, CreateView):
#     model = Students
#     form_class = StudentForm

#     def get_context_data(self, **kwargs):
#         context = super(StudentCreateView, self).get_context_data(**kwargs)
#         context['main_page_title'] = 'Student Creation'
#         context['panel_name'] = 'pnameStudents'
#         context['panel_title'] = 'pttlCreate Student'
#         return context







def register(request):
    print("regpost method")
    if request.method == 'POST':
        print(" if post method")
        sfname = request.POST.get('sfname', '')
        slname = request.POST.get('slname', '')
        semail = request.POST.get('semail', '')
        spass = request.POST.get('spass', '')
        suser = request.POST.get('suser', '')    
        # print("sfname=",sfname,"semail=",semail,"spass=",spass)
        print("sfname=",sfname,"semail=",semail,"spass=",spass,"suser=",suser)
        # emp = Students(eid=sfname, ename=slname, epass=spass, email=semail)
        emp = Students(suser=suser,eid=sfname, ename=slname, epass=spass, email=semail)

        emp.save()
        return redirect("/login")
    return render(request,"users/registerr.html")




@login_required(login_url='sb_admin_register')
def start(request):
    """Start page with a documentation.
    """
    return render(
        request,
        "django_sb_admin/start.html",
        {
            "nav_active": "start"
        }
    )


def login(request):
    print("loginpost method")
    if request.method == 'POST':
        print("loginpost")
        em=request.POST.get('email','')
        ep=request.POST.get('epass','')
        students = Students.objects.get(email=em)
        if students.email==em and students.epass==ep:
                    request.session['semail'] = em
                    print("logined to account with email=",em,"pass=",ep)
                    return redirect("/dashboard/")
        else:
                    print("password not correct else login")
                    messages.info(request, 'Username OR password is incorrect')
                    return redirect("/login")

    return render(request,"django_sb_admin/login.html")
    

def logout(request):
    return render(request,"django_sb_admin/logout.html")


# def logout(request):
#    try:
#       del request.session['username']
#    except:
#       pass
#    return redirect("/")



    #     user = Students.authenticate(username=email, password=loginpassword)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request,"successfully logged in")
    #         return redirect('home')
    #     else:
    #         messages.error(request,"Invalid credentials, please try again")
    #         return redirect('home')

    # return HttpResponse('404- Not Found')

    #  if id==1:
    #     em=request.POST.get('email','')
    #     ep=request.POST.get('epass','')
    #     if em!='':
    #         try:
    #             employee = Employee.objects.get(email=em)

    #             if employee.email==em and employee.epass==ep:
    #                 request.session['username'] = em
    #                 print("logined to account with email=",em,"pass=",ep)
    #                 return redirect("/show")
    #             else:
    #                 print("password not correct else login")
    #                 return redirect("/login")
    #         except:
    #             print("exception")
    #             return redirect("/login")
    #     else:
    #         print("Email password not blank else em!=")
    #         return render(request,"login.html")

    # return render(request,"login.html")













def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("Validation Success !")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Password: "+form.cleaned_data['password'])
            print("Text: "+form.cleaned_data['text'])
            
            messages.success(request, f'Your account has been created! You are now able to log in')
            messages.success(request,"successfully logged in")
            return redirect('user_register')
    else:
        form = UserRegisterForm()
        context = {'form' :form}

    return render(request, 'django_sb_admin/users/register.html', context)



def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("\nUser Name = ",username)
        print("Password = ",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {'message':'Invalid User Name and Password'}
            return render(request, 'index.html', context)
    return render(request, 'index.html')

class Login(View):
    template = 'login.html'
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})




@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'info/t_homepage.html')
    if request.user.is_student:
        return render(request, 'info/homepage.html')
    return render(request, 'info/logout.html')

def show(request,uname=''):
    employees=Employee.objects.all()
    print(employees)

    if request.session.has_key('username'):
        uname = request.session['username']
        return render(request,"show.html",{'employees':employees,'uname':uname})
    else:
        return redirect("/")

def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'inv/index.html', context)



def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee' : employee } )


def update(request, id):
    employee = Employee.objects.get(id=id)
    eidd=employee.id

    employee.eid = request.POST.get('eid', '')
    employee.ename= request.POST.get('ename', '')
    employee.email = request.POST.get('email', '')
    employee.econtact = request.POST.get('econtact', '')
    employee.eimg = request.FILES.get('mfile')
    print("emage=",employee.eimg)
    employee.eimg.name=str(eidd)+'.jpg'

    image_path = settings.MEDIA_ROOT + '/app/img/'+str(eidd)+'.jpg'


    if os.path.isfile(image_path):
        os.remove(image_path)
# # 
    employee.save()
    return redirect("/show")







def delete(request, id):

    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")






@login_required(login_url='signin')
def dashboard(request):
    """Dashboard page.
    """
        # if request.session['semail']:
    # context = super().get_context_data(**kwargs)
    # context['member'] = MemberProfile.objects.count()
    # print(context['member'])
    # context['book'] = Book.objects.count()
    # context['lib'] = LibrarianProfile.objects.count()
    # context['trans'] = Transaction.objects.count()
    

    # items = Employee.objects.all()
    # context = Employee.objects.all()
    # {
    #     'items': items,
    # }



    print("hii")
    # template_name = "django_sb_admin/sb_admin_dashboard.html"

    
    # def get_context_data(self, **kwargs):
    #     context = super(dashboard, self).get_context_data(**kwargs)
    #     context['member'] = MemberProfile.objects.count()
    #     print(context['member'])
    #     context['book'] = Book.objects.count()
    #     context['lib'] = LibrarianProfile.objects.count()
    #     context['trans'] = Transaction.objects.count()
    #     return context
    

    if request.user.is_superuser:
        employees = models.Students.objects.all()
        count=models.MemberProfile.objects.all().count()
        users = User.objects.count()

        mydict={
        'count':count,
        'employees': employees,
        'users':users
    }
        return render(request,"django_sb_admin/sb_admin_dashboard.html",context=mydict )
    elif request.user.is_staff:
        return render(request,"index.html" )
    else :
        return HttpResponse("You are student")
   
    # return render(
    #     request,
    #     "django_sb_admin/sb_admin_dashboard.html",
    #     {
    #         "nav_active": "dashboard"
    #     }
    #     # ,context
    # )

def charts(request):
    """Charts page.
    """
    return render(request, "django_sb_admin/sb_admin_charts.html",
                  {"nav_active":"charts"})
def tables(request):
    """Tables page.
    """
    employees = MemberProfile.objects.all()
    return render(request,"django_sb_admin/sb_admin_tables.html", {'employees': employees})

    # return render(request, "django_sb_admin/sb_admin_tables.html",
    #               {"nav_active":"tables"})

def approve(request):
    """Tables page.
    """
    employees = MemberProfile.objects.all()
    return render(request,"django_sb_admin/approve_registration.html", {'employees': employees})

def forms(request):
    """Forms page.
    """
    return render(request, "django_sb_admin/sb_admin_forms.html",
                  {"nav_active":"forms"})
def bootstrap_elements(request):
    """Bootstrap elements page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_elements.html",
                  {"nav_active":"bootstrap_elements"})
def bootstrap_grid(request):
    """Bootstrap grid page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_grid.html",
                  {"nav_active":"bootstrap_grid"})
def dropdown(request):
    """Dropdown  page.
    """
    return render(request, "django_sb_admin/sb_admin_dropdown.html",
                  {"nav_active":"dropdown"})
def rtl_dashboard(request):
    """RTL Dashboard page.
    """
    return render(request, "django_sb_admin/sb_admin_rtl_dashboard.html",
                  {"nav_active":"rtl_dashboard"})

def blank(request):
    """Blank page.
    """
    employees = MemberProfile.objects.all()
    return render(request,"django_sb_admin/sb_admin_blank.html", {'employees': employees})
