from django.shortcuts import render
from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
	print ("isme ghusa ya nhi?")
	jobs = Job.objects
	print("Ye hai jobs bandhuon ", jobs)
	return render(request, 'job/home.html' , {'jobs' : jobs})