from django.contrib import admin
from .forms import JobForm

# Register your models here.

from .models import Administrator,Supervisor,Employee,Job,Report

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
	form = JobForm
	list_filter = ['name','added']
	filter_horizontal = ('jobemployee',)
	list_display = ['name','added']
	class Meta:
		model = Job

class ReportAdmin(admin.ModelAdmin):
	list_display = ['heading','date','sender']
	list_filter = ['date']
	class Meta:
		model = Report

admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Supervisor,SupervisorAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Report,ReportAdmin)