from django import forms
from .models import Employee,Job


class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['name','deadline','userRequired','jobemployee','description','status','difficulty','submitrequest','department']

	def clean_jobemployee(self):
		userRequired = self.cleaned_data.get('userRequired')
		department = self.cleaned_data.get('department') 
		users = Employee.objects.all().order_by('-job_count')[:userRequired]
		for user in users:
			user.job_count += 1

		return users