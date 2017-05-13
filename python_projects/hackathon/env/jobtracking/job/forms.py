from django import forms
from .models import User,Job


class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['name','deadline','userRequired','user','description','status','difficulty','submitrequest','department']

	def clean_user(self):
		userRequired = self.cleaned_data.get('userRequired')
		department = self.cleaned_data.get('department') 
		users = User.objects.filter(role=2).order_by('job_count')
		if len(users) >= userRequired:
			users = users[:userRequired]
		for user in users:
			user.job_count += 1
			user.save()

		return users