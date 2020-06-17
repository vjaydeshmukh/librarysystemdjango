from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile
from . import models
# from labb.models import
# from student_management_app.models import Courses

# from .models import Member

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(SignupForm, self).save(commit=False)
            user.email = cleaned_data['email']
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']

            if commit:
                user.save()

            return user




# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = Member
#         fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'status', 'address', 'city',
#                   'province', 'photo', 'auto_renew']            

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['roll','cl','mobile','fee','status']

class StudentUserForm1(forms.ModelForm):
    class Meta:
        model=User
        fields=['username']
    # def __init__(self, *args, **kwargs):
    #     super(StudentUserForm1,self).__init__(*args, **kwargs)
    #     self.fields['username'].empty_label = "Select"
    
class StudentExtraForm1(forms.ModelForm):
    class Meta:
        model=models.MemberProfile
        fields=['user_name','prn','phone','eimg','address','age','gender','birth_date','year','branch']


    # def __init__(self, *args, **kwargs):
    #     super(StudentExtraForm1,self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = "Select"


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']



# class StudentAddForm(UserCreationForm):
#     username = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'text',
#                 'class': 'form-control',
#             }
#         ),
#         label = "Username",
#     )
#     address = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'text',
#                 'class': 'form-control',
#             }
#         ),
#         label = "Address",
#     )

#     phone = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'text',
#                 'class': 'form-control',
#             }
#         ),
#         label = "Mobile No.",
#     )

#     firstname = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'text',
#                 'class': 'form-control',
#             }
#         ),
#         label = "Firstname",
#     )

#     lastname = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'text',
#                 'class': 'form-control',
#             }
#         ),
#         label = "Lastname",
#     )

#     level = forms.CharField(
#         widget=forms.Select(
#             choices = LEVEL,
#             attrs={
#                 'class': 'browser-default custom-select',
#             }
#         ),
#     )

#     email = forms.EmailField(
#         widget=forms.TextInput(
#             attrs={
#                 'type': 'email',
#                 'class': 'form-control',
#             }
#         ),
#         label = "Email Address",
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User


#     @transaction.atomic()
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.first_name=self.cleaned_data.get('firstname') 
#         user.last_name=self.cleaned_data.get('lastname')
#         user.phone=self.cleaned_data.get('phone')
#         user.email=self.cleaned_data.get('email')
#         user.save()
#         student = Student.objects.create(user=user, id_number=user.username, level=self.cleaned_data.get('level'))
#         student.save()
#         return user





# class AddStudentForm(forms.Form):
#     email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
#     password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
#     first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
#     last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
#     username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
#     address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

#     courses=Courses.objects.all()
#     course_list=[]
#     for course in courses:
#         small_course=(course.id,course.course_name)
#         course_list.append(small_course)

#     gender_choice=(
#         ("Male","Male"),
#         ("Female","Female")
#     )

#     course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
#     sex=forms.ChoiceField(label="Sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
#     session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
#     session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
#     profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))
