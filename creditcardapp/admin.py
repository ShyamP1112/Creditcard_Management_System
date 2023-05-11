from django.contrib import admin
from .models import  usersignup,creditcardapply,contacts
# Register your models here.

class signupModel(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','mobile','password']

admin.site.register(usersignup,signupModel)

class creditcardapplyModel(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','fname','mname','lname','email','mobile','mothername','jobdesignation','sallary','birthdate','address','city','pincode','aadharcard','pancard','userimages','bankstatement','sllaryslip','selectbank','gender']

admin.site.register(creditcardapply,creditcardapplyModel)


class contactModel(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','phonenumber','email','massage']

admin.site.register(contacts,contactModel)