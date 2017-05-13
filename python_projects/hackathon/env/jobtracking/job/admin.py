from django.contrib import admin
from.models import User,Job,Part,Report
from .forms import JobForm
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['name','added']
	list_filter = ['added']
	class Meta:
		model = User

class JobAdmin(admin.ModelAdmin):
	form = JobForm
	list_filter = ['added']
	list_display = ['name','added']
	filter_horizontal = ('user',)
	class Meta:
		model = Job

class PartAdmin(admin.ModelAdmin):
	list_filter = ['name','added']
	list_display = ['name','job','added']
	class Meta:
		model = Part


class ReportAdmin(admin.ModelAdmin):
	list_filter = ['title','sender']
	list_display = ['title','added']
	class Meta:
		model = Report


admin.site.register(User,UserAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Part,PartAdmin)
admin.site.register(Report,ReportAdmin)

