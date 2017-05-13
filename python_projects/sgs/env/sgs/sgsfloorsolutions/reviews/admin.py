from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
	list_display = ["username","added"]
	list_filter = ["added"]

	class Meta:
		model = Review


admin.site.register(Review,ReviewAdmin)
