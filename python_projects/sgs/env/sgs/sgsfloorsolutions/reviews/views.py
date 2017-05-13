
from django.shortcuts import render,get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
	context = {}
	return render(request,"index.html",context)

def floor_maintenance(request):
	context = {}
	return render(request,"floor_maintenance.html",context)

def densification(request):
	context = {}
	return render(request,"densification.html",context)

def floor_solutions(request):
	context = {}
	return render(request,"floor_solutions.html",context)

def floor_preparations(request):
	context = {}
	return render(request,"floor_preparations.html",context)

def contact_us(request):
	form = ReviewForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request,"Congratulations!! Your input has been saved.")
			return HttpResponseRedirect("/contact_us")
		else:
			messages.error(request,"Incorrect form data.")
			return HttpResponseRedirect("/contact_us")

	else:
		context = {
			"form":form,
		}
		return render(request,"contact.html",context)
