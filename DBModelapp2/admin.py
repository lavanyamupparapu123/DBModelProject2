from django.contrib import admin
from DBModelapp2.models import Employee2
from DBModelapp2.models import Job
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr'];


admin.site.register(Employee2,EmployeeAdmin);


class JobAdmin(admin.ModelAdmin):
    list_display=['postingdate','location','offeredsalary','qualification'];



