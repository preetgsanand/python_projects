from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
	class Meta:
		model  = Review
		fields = ["username","email","content"]

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if len(username) < 5:
			raise forms.ValidationError("Please enter your full name")
		else:
			return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if "@" in email:
			return email;
		else:
			raise forms.ValidationError("Sorry, Incorrect email")