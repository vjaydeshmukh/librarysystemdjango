from django.contrib import admin
from .models import MemberProfile
from import_export.admin import ImportExportModelAdmin

# No admin fews here
from .models import Students,StudentExtra
from . import models
# from django.contrib.auth.models import User

class MemberProfileAdmin(ImportExportModelAdmin):
    fields = ['username','user_name','eimg','prn' ,'phone', 'address', 'age', 'gender', 'birth_date','year','branch']
    list_display = ['username','user_name','eimg','prn' , 'phone', 'address', 'age', 'gender', 'birth_date','year','branch']
    search_fields  = ['phone']
    list_filter = ['gender', 'age']




class StudentsAdmin(admin.ModelAdmin):

	fields = ['suser','eid', 'ename', 'epass','email','eimg','econtact']
	
	list_display =  ['suser','eid', 'ename', 'epass','email','eimg','econtact','date_created']



admin.site.register(models.Students, StudentsAdmin)

class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)
admin.site.register(models.MemberProfile, MemberProfileAdmin)
admin.site.register(models.Position)
