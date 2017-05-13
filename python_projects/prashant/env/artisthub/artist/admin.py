from django.contrib import admin


from .models import Artist,User
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
	list_display = ["name","updated"]
	list_filter = ["added","updated"]
	class Meta:
		model = Artist

class UserAdmin(admin.ModelAdmin):
	list_display = ["name","updated"]
	list_filter = ["added","updated"]
	class Meta:
		model = User

admin.site.register(Artist,ArtistAdmin)
admin.site.register(User,UserAdmin)
