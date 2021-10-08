from django.contrib import admin
from .models import Employee

# Register your models here.
#admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('name', 'position', 'salary', 'employment_date', 'parent')

admin.site.register(Employee, EmployeeAdmin)