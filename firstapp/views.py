from django.shortcuts import render ,HttpResponse
from datetime import datetime
from firstapp.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
	
	return render(request,'index.html',)
	

def apply(request):
	return render(request,'apply.html')

def about(request):
	return render(request,'about.html')

def socials(request):
	return render(request,'social.html')

def contact(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		subject = request.POST.get("subject")
		message= request.POST.get("message")
		contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
		contact.save()
		messages.success(request, 'Your message has been sent')
	return render(request,'contact.html')