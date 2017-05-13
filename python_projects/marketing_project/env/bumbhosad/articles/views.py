
from django.shortcuts import render,get_object_or_404
from .models import Article,Review
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm

# Create your views here.

def index(request):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	else:
		top_stories = Article.objects.order_by('-visitors_count')[:5]
		recent_stories = Article.objects.order_by('-added')[:5]
		health = Article.objects.filter(category=1)[:4]
		politics = Article.objects.filter(category=2)[:4]
		entertainment = Article.objects.filter(category=3)[:4]
		first = Article.objects.latest('added')
		context = {
			"top_stories":top_stories,
			"recent_stories":recent_stories,
			"first":first,
			'health': health,
			'politics' : politics,
			'entertainment':entertainment,
		}
		return render(request, 'index.html', context)


def health(request):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	queryset = Article.objects.filter(category=1).order_by('-added')
	first = queryset.order_by('-visitors_count')[0]
	context = {
		"first":first,
		'queryset': queryset,
		'title' : "HEALTH",
	}
	return render(request, 'list.html', context)

def politics(request):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	queryset = Article.objects.filter(category=2).order_by('-added')
	first = queryset.order_by('-visitors_count')[0]
	context = {
		"first":first,
		'queryset': queryset,
		'title' : "POLITICS",
	}
	return render(request, 'list.html', context)

def search(request,query):
	query_all = Article.objects.all()
	queryset = query_all.filter(title__icontains=query)
	context = {
		"query":query,
		"queryset":queryset,
		"title":"SEARCH RESULTS"
	}
	return render(request, 'search.html', context)


def entertainment(request):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	queryset = Article.objects.filter(category=3).order_by('-added')
	first = queryset.order_by('-visitors_count')[0]
	context = {
		"first":first,
		'queryset': queryset,
		'title' : "ENTERTAINMENT",
	}
	return render(request, 'list.html', context)

def finance(request):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	queryset = Article.objects.filter(category=4).order_by('-added')
	first = queryset.order_by('-visitors_count')[0]
	context = {
		"first":first,
		'queryset': queryset,
		'title' : "FINANCE",
	}
	return render(request, 'list.html', context)

def loans(request):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	queryset = Article.objects.filter(category=5).order_by('-added')
	first = queryset.order_by('-visitors_count')[0]
	context = {
		"first":first,
		'queryset': queryset,
		'title' : "LOANS",
	}
	return render(request, 'list.html', context)

def detail(request,id):
	if request.GET.get("q"):
		return search(request,request.GET.get("q"))
	queryset = Article.objects.order_by('-visitors_count')[:4]
	might_also = Article.objects.order_by('-added')[:8]
	query = get_object_or_404(Article,id=id)
	query.visitors_count += 1
	query.save()
	context = {
		'might_also':might_also,
		'queryset':queryset,
		"query":query,
	}
	return render(request, "detail.html", context)

def contact(request):
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