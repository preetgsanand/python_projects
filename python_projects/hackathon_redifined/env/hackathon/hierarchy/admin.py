from django.contrib import admin

# Register your models here.

from .models import Administrator,Supervisor,Employee,Job

class AdministratorAdmin(admin.ModelAdmin):
	list_display = ['name','added']
	list_filter = ['added']
	class Meta:
		model = Administrator

class SupervisorAdmin(admin.ModelAdmin):
	list_display = ['name','added','administrator']
	list_filter = ['added']
	class Meta:
		model = Supervisor

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['name','added','supervisor']
	list_filter = ['added']
	class Meta:
		model = Employee

class JobAdmin(admin.ModelAdmin):
	list_filter = ['name','added']
	list_display = ['name','added']
	class Meta:
		model = Job

admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Supervisor,SupervisorAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Job,JobAdmin)