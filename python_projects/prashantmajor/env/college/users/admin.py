from django.contrib import admin

from .models import Entity,Role,Department,Block,Room,Batch,Period
# Register your models here.


class RoleAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Role

class EntityAdmin(admin.ModelAdmin):
	list_display = ['name','added']
	list_filter = ['added','department']
	filter_horizontal = ('role',)
	class Meta:
		model = Entity

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Department

class BatchAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	class Meta:
		model = Batch

class BlockAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Block

class RoomAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Room

class PeriodAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	class Meta:
		model = Period

admin.site.register(Entity,EntityAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Period,PeriodAdmin)
