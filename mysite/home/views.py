from django.http import HttpResponse
from django.shortcuts import render

from home.models import Contact
from django.contrib import messages

# from home.models import Contact


# Create your views here.
def index(request):
    context = {
        'variable' : "This is Aadesh"
    }
    return render(request,'index.html',context)
    
    # return HttpResponse("This is index page")

def about(request):
    return render(request,'about.html')

def services(request):
   return render(request,'services.html')

def contact(request):
    # print(request.objects.all())
   if(request.method=='POST'):
        name  = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        details = Contact(name=name,email=email,phone=phone)
        details.save()
        messages.success(request, 'Your Message Has been Sent!!!.')
   return render(request,'contact.html')