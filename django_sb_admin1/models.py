from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class MemberProfile(models.Model):
	username = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	# PRN = models.CharField(max_length=8, default=0)
	user_name = models.CharField(max_length=30)
	prn = models.CharField(max_length=10,default=0)
	eimg = models.ImageField(upload_to='app/img')

	phone = models.CharField(max_length=13)
	address = models.CharField(max_length=200, default=None)
	age = models.PositiveSmallIntegerField(default=0)
	# position= models.ForeignKey(Position,on_delete=models.CASCADE)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	birth_date = models.DateField(null=True, blank=True)
	YEAR_CHOICES = (('FY', '1st year'), ('DSY', 'Direct 2nd year'), ('SY', '2nd year'), ('TY', '3rd year'), ('LY', '4th year'))
	year = models.CharField(max_length=3, choices=YEAR_CHOICES, default='M')
	BRANCH_CHOICES = (('ME', 'Mechanical'), ('CE', 'Civil'), ('EE', 'Electrical'), ('ENTC', 'Elect. & Tele. Communication'), ('IE', 'Instrumentation'), ('CO', 'Computer'), ('IT', 'INfo. Tech'))
	branch = models.CharField(max_length=4, choices=BRANCH_CHOICES, default='M')
	book_limit = models.PositiveSmallIntegerField(default=5)
    

	def __str__(self):
		return self.username.username

# Create your models here.
class Students(models.Model):
    eid=models.CharField(max_length=30)
    ename=models.CharField(max_length=100)
    epass = models.CharField(max_length=100)
    email=models.EmailField()
    eimg = models.FileField(upload_to='app/img')
    econtact=models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    suser=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	# profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	


classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.roll

# class Book(models.Model):
#     CATEGORY_CHOICES = [
#         ('S', 'Scinece&Tech'),
#         ('F', 'Fiction'),
#         ('B', 'Biography'),
#         ('T', 'Travel'),
#         ('O', 'Other')
#     ]
#     title = models.CharField(max_length=200)
#     category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='S')
#     description = models.TextField(blank=True)
#     num_pages = models.PositiveIntegerField(default=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
#     publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
#     num_reviews = models.PositiveIntegerField(default=0)
#     book_photo = models.ImageField(upload_to='photos/%Y/%m/%d/book/', blank= True)
#     def __str__(self):
#         return self.title



# class Member(User):
#     STATUS_CHOICES = [
#         (1, 'Regular member'),
#         (2, 'Premium Member'),
#         (3, 'Guest Member'),
#     ]
#     status = models.IntegerField(choices=STATUS_CHOICES, default=1)
#     address = models.CharField(max_length=300, blank=True)
#     city = models.CharField(max_length=20,default="Windsor")
#     province=models.CharField(max_length=2, default='ON')
#     last_renewal = models.DateField(default=timezone.now)
#     auto_renew = models.BooleanField(default=True)
#     borrowed_books = models.ManyToManyField(Book, blank=True)
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/member/', blank=True)
#     def __str__(self):
#         return self.first_name
#     def books_borrowed(self):
#         return ", ".join([str(p) for p in self.borrowed_books.all()])
#     @property
#     def get_photo_url(self):
#         if self.photo and hasattr(self.photo, 'url'):
#             return self.photo.url

    


# class Students(models.Model):
#     id=models.AutoField(primary_key=True)
#     admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
#     gender=models.CharField(max_length=255)
#     profile_pic=models.FileField()
#     address=models.TextField()
#     course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
#     session_start_year=models.DateField()
#     session_end_year=models.DateField()
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()
