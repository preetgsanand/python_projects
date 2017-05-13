from django.contrib import admin
from .models import Article,Review
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ["title","added","category"]
	list_filter = ["added","updated"]
	class Meta:
		model = Article

class ReviewAdmin(admin.ModelAdmin):
	list_display = ["username","added"]
	list_filter = ["added"]

	class Meta:
		model = Review


admin.site.register(Review,ReviewAdmin)

admin.site.register(Article,ArticleAdmin)
