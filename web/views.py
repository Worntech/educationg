from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from pesapal.views import *

# FOR PAYMENT
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView

from django_pesapal.views import PaymentRequestMixin

from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment, Websitetemplate
from decimal import Decimal

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'web/admin.html')
def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                # messages.info(request, 'Registered succesefull.')
                return redirect('signupsucces')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'web/signup.html')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    # messages.info(request, 'Loged out succesefull.')
    return redirect('logedout')


def home(request):
    return render(request, 'web/home.html')
def aboutus(request):
    return render(request, 'web/aboutus.html')
def base(request):
    return render(request, 'web/base.html')
def contactus(request):
    return render(request, 'web/contactus.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('name')
        Subject = request.POST.get('subject')
        Email = request.POST.get('email')
        Message = request.POST.get('message')
        Phone = request.POST.get('phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            messages.info(request, 'Message sent succesefull.')
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
@login_required(login_url='signin')
def contactlist(request):
    contactlist = Contact.objects.all()
    countmessage= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "countmessage":countmessage
    }
    return render(request, 'web/contactlist.html', context)
@login_required(login_url='signin')
def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)
@login_required(login_url='signin')
def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        messages.info(request, 'Message deleted succesefull.')
        return redirect('contactlist')
    
    context = {"contact":contact}
    return render(request, 'web/deletecontact.html', context)


@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'web/dashboard.html')

def services(request):
    return render(request, 'web/services.html')

# courses to be tought
# @login_required(login_url='signin')
def computercs(request):
    return render(request, 'web/computercs.html')
# @login_required(login_url='signin')
def computereng(request):
    return render(request, 'web/computereng.html')
# @login_required(login_url='signin')
def electrical(request):
    return render(request, 'web/electrical.html')
# @login_required(login_url='signin')
def civil(request):
    return render(request, 'web/civil.html')
# @login_required(login_url='signin')
def mechanical(request):
    return render(request, 'web/mechanical.html')
# @login_required(login_url='signin')
def artificial(request):
    return render(request, 'web/artificial.html')
# @login_required(login_url='signin')
def softwareeng(request):
    return render(request, 'web/softwareeng.html')
# @login_required(login_url='signin')
def embeded(request):
    return render(request, 'web/embeded.html')
# @login_required(login_url='signin')
def website(request):
    return render(request, 'web/website.html')
# @login_required(login_url='signin')
def mobileapp(request):
    return render(request, 'web/mobileapp.html')
# @login_required(login_url='signin')
def virtualreality(request):
    return render(request, 'web/virtualreality.html')
# @login_required(login_url='signin')
def security(request):
    return render(request, 'web/security.html')
# @login_required(login_url='signin')
def desktopapp(request):
    return render(request, 'web/desktopapp.html')
# @login_required(login_url='signin')
def multmedia(request):
    return render(request, 'web/multmedia.html')
# @login_required(login_url='signin')
def graphics(request):
    return render(request, 'web/graphics.html')
# @login_required(login_url='signin')
def iot(request):
    return render(request, 'web/iot.html')
# @login_required(login_url='signin')
def security(request):
    return render(request, 'web/security.html')
# @login_required(login_url='signin')
def nertworking(request):
    return render(request, 'web/nertworking.html')

# views for success message
def signupsucces(request):
    return render(request, 'web/signupsucces.html')
def logedout(request):
    return render(request, 'web/logedout.html')

# for website frontend development
# @login_required(login_url='signin')
def wfrontend(request):
    return render(request, 'web/wfrontend.html')

# @login_required(login_url='signin')
def htmlcss(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/htmlcss.html',context)

# @login_required(login_url='signin')
def javascript(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/javascript.html',context)

# @login_required(login_url='signin')
def reactjs(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/reactjs.html',context)

# @login_required(login_url='signin')
def vuejs(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/vuejs.html',context)

# @login_required(login_url='signin')
def bootstrap(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/bootstrap.html',context)

# @login_required(login_url='signin')
def angularjs(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/angularjs.html',context)

# for website backend development
# @login_required(login_url='signin')
def wbackend(request):
    return render(request, 'web/wbackend.html')

# @login_required(login_url='signin')
def django(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/django.html',context)

# @login_required(login_url='signin')
def flask(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/flask.html',context)

# @login_required(login_url='signin')
def php(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/php.html',context)

# @login_required(login_url='signin')
def laravel(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/laravel.html',context)

# @login_required(login_url='signin')
def rub(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/rub.html',context)

# for full stack website development
# @login_required(login_url='signin')
def wfullstack(request):
    return render(request, 'web/wfullstack.html')

# @login_required(login_url='signin')
def djangohtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/djangohtml.html',context)

# @login_required(login_url='signin')
def flaskhtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/flaskhtml.html',context)

# @login_required(login_url='signin')
def phphtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/phphtml.html',context)

# @login_required(login_url='signin')
def laravelhtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/laravelhtml.html',context)

# @login_required(login_url='signin')
def djangoreact(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/djangoreact.html',context)

# for mobile application frontend
# @login_required(login_url='signin')
def mfrontend(request):
    return render(request, 'web/mfrontend.html')

# @login_required(login_url='signin')
def reactnative(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnative.html',context)

# @login_required(login_url='signin')
def kivy(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/kivy.html',context)
# @login_required(login_url='signin')
def fluter(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/fluter.html',context)

#for mobile application backnd development
# @login_required(login_url='signin')
def mbackend(request):
    return render(request, 'web/mbackend.html')

# @login_required(login_url='signin')
def mdjango(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/django.html',context)

# @login_required(login_url='signin')
def mflask(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/flask.html',context)

# @login_required(login_url='signin')
def mfirebase(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/firebase.html',context)

#for mobile application full stack development
# @login_required(login_url='signin')
def mfullstack(request):
    return render(request, 'web/mfullstack.html')

# @login_required(login_url='signin')
def reactnativedjango(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnativedjango.html',context)

# @login_required(login_url='signin')
def reactnativeflask(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnativeflask.html',context)

# @login_required(login_url='signin')
def reactnativefirebase(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnativefirebase.html',context)

# for desktop application
# @login_required(login_url='signin')
def cdeskapp(request):
    desktop = Desktop.objects.all()
    context={
        "desktop":desktop
    }
    return render(request, 'web/cdeskapp.html',context)
# @login_required(login_url='signin')
def pdeskapp(request):
    desktop = Desktop.objects.all()
    context={
        "desktop":desktop
    }
    return render(request, 'web/pdeskapp.html',context)

# @login_required(login_url='signin')
def kdeskapp(request):
    desktop = Desktop.objects.all()
    context={
        "desktop":desktop
    }
    return render(request, 'web/kdeskapp.html',context)

# for embeded system
# @login_required(login_url='signin')
def cembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/cembeded.html',context)
# @login_required(login_url='signin')
def aembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/aembeded.html',context)

# @login_required(login_url='signin')
def pembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/pembeded.html',context)

# @login_required(login_url='signin')
def mpembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/mpembeded.html',context)

# for graphics designing
# @login_required(login_url='signin')
def photoshop(request):
    graphics = Graphics.objects.all()
    context={
        "graphics":graphics
    }
    return render(request, 'web/photoshop.html',context)

# @login_required(login_url='signin')
def illustrator(request):
    graphics = Graphics.objects.all()
    context={
        "graphics":graphics
    }
    return render(request, 'web/illustrator.html',context)


# FOR PROJECT
# @login_required(login_url='signin')
def websiteproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/websiteproject.html',context)

# @login_required(login_url='signin')
def mobileproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/mobileproject.html',context)

# @login_required(login_url='signin')
def desktopproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/desktopproject.html',context)

# @login_required(login_url='signin')
def artificialproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/artificialproject.html',context)

# @login_required(login_url='signin')
def embededproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/embededproject.html',context)

# @login_required(login_url='signin')
def iotproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/iotproject.html',context)

# @login_required(login_url='signin')
def virtualrealityproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/virtualrealityproject.html',context)

# @login_required(login_url='signin')
def cyberproject(request):
    project = Project.objects.all()
    context={
        "project":project
    }
    return render(request, 'web/cyberproject.html',context)

# @login_required(login_url='signin')
def image(request):
    image = Image.objects.all()
    context={
        "image":image
    }
    return render(request, 'web/image.html',context)

# template download
# @login_required(login_url='signin')
def webtemplate(request):
    return render(request, 'web/webtemplate.html')

# @login_required(login_url='signin')
def htmlcsstemplate(request):
    websitetemplate = Websitetemplate.objects.all()
    context={
        "websitetemplate":websitetemplate,
    }
    return render(request, 'web/htmlcsstemplate.html',context)

# @login_required(login_url='signin')
def reacttemplate(request):
    websitetemplate = Websitetemplate.objects.all()
    context={
        "websitetemplate":websitetemplate
    }
    return render(request, 'web/reacttemplate.html',context)


# @login_required(login_url='signin')
def mobiletemplate(request):
    return render(request, 'web/mobiletemplate.html')

# @login_required(login_url='signin')
def reactnativetemplate(request):
    mobiletemplate = Mobiletemplate.objects.all()
    context={
        "mobiletemplate":mobiletemplate
    }
    return render(request, 'web/reactnativetemplate.html',context)


# @login_required(login_url='signin')
def desktoptemplate(request):
    return render(request, 'web/desktoptemplate.html')

# @login_required(login_url='signin')
def kivytemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/kivytemplate.html',context)

# @login_required(login_url='signin')
def pyqttemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/pyqttemplate.html',context)

# @login_required(login_url='signin')
def ctemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/ctemplate.html',context)

# @login_required(login_url='signin')
def tkintertemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/tkintertemplate.html',context)


# @login_required(login_url='signin')
def microsofttemplate(request):
    return render(request, 'web/microsofttemplate.html')

# @login_required(login_url='signin')
def wordtemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/wordtemplate.html',context)

# @login_required(login_url='signin')
def excelltemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/excelltemplate.html',context)

# @login_required(login_url='signin')
def powerpointtemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/powerpointtemplate.html',context)

# @login_required(login_url='signin')
def publishertemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/publishertemplate.html',context)


# @login_required(login_url='signin')
def adobetemplate(request):
    return render(request, 'web/adobetemplate.html')

# @login_required(login_url='signin')
def photoshoptemplate(request):
    adobetemplate = Adobetemplate.objects.all()
    context={
        "adobetemplate":adobetemplate
    }
    return render(request, 'web/photoshoptemplate.html',context)

# @login_required(login_url='signin')
def primiertemplate(request):
    adobetemplate = Adobetemplate.objects.all()
    context={
        "adobetemplate":adobetemplate
    }
    return render(request, 'web/primiertemplate.html',context)

# @login_required(login_url='signin')
def illustratortemplate(request):
    adobetemplate = Adobetemplate.objects.all()
    context={
        "adobetemplate":adobetemplate
    }
    return render(request, 'web/illustratortemplate.html',context)
    
# download image


# for posting the course and the template to the website
@login_required(login_url='signin')
def websitepost(request):
    websitepost = WebsiteForm()
    if request.method == "POST":
        websitepost = WebsiteForm(request.POST, files=request.FILES)
        if websitepost.is_valid():
            websitepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('websitepost')
    context={
        "websitepost":websitepost
    }
    return render(request, 'web/websitepost.html',context)

@login_required(login_url='signin')
def mobilepost(request):
    mobilepost = MobileForm()
    if request.method == "POST":
        mobilepost = MobileForm(request.POST, files=request.FILES)
        if mobilepost.is_valid():
            mobilepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('mobilepost')
    context={
        "mobilepost":mobilepost
    }
    return render(request, 'web/mobilepost.html',context)

@login_required(login_url='signin')
def desktoppost(request):
    desktoppost = DesktopForm()
    if request.method == "POST":
        desktoppost = DesktopForm(request.POST, files=request.FILES)
        if desktoppost.is_valid():
            desktoppost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('desktoppost')
    context={
        "desktoppost":desktoppost
    }
    return render(request, 'web/desktoppost.html',context)

@login_required(login_url='signin')
def embededpost(request):
    embededpost = EmbededForm()
    if request.method == "POST":
        embededpost = EmbededForm(request.POST, files=request.FILES)
        if embededpost.is_valid():
            embededpost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('embededpost')
    context={
        "embededpost":embededpost
    }
    return render(request, 'web/embededpost.html',context)

@login_required(login_url='signin')
def graphicspost(request):
    graphicspost = GraphicsForm()
    if request.method == "POST":
        graphicspost = GraphicsForm(request.POST, files=request.FILES)
        if graphicspost.is_valid():
            graphicspost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('graphicspost')
    context={
        "graphicspost":graphicspost
    }
    return render(request, 'web/graphicspost.html',context)

# POST PROJECT
@login_required(login_url='signin')
def projectpost(request):
    projectpost = ProjectForm()
    if request.method == "POST":
        projectpost = ProjectForm(request.POST, files=request.FILES)
        if projectpost.is_valid():
            projectpost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('projectpost')
    context={
        "projectpost":projectpost
    }
    return render(request, 'web/projectpost.html',context)

# POST IMAGE
@login_required(login_url='signin')
def imagepost(request):
    imagepost = ImageForm()
    if request.method == "POST":
        imagepost = ImageForm(request.POST, files=request.FILES)
        if imagepost.is_valid():
            imagepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('imagepost')
    context={
        "imagepost":imagepost
    }
    return render(request, 'web/imagepost.html',context)

# for posting template
@login_required(login_url='signin')
def websitetemplatepost(request):
    websitetemplatepost = WebsitetemplateForm()
    if request.method == "POST":
        websitetemplatepost = WebsitetemplateForm(request.POST, files=request.FILES)
        if websitetemplatepost.is_valid():
            websitetemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('websitetemplatepost')
    context={
        "websitetemplatepost":websitetemplatepost
    }
    return render(request, 'web/websitetemplatepost.html',context)

@login_required(login_url='signin')
def mobiletemplatepost(request):
    mobiletemplatepost = MobiletetemplateForm()
    if request.method == "POST":
        mobiletemplatepost = MobiletetemplateForm(request.POST, files=request.FILES)
        if mobiletemplatepost.is_valid():
            mobiletemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('mobiletemplatepost')
    context={
        "mobiletemplatepost":mobiletemplatepost
    }
    return render(request, 'web/mobiletemplatepost.html',context)

@login_required(login_url='signin')
def desktoptemplatepost(request):
    desktoptemplatepost = DesktoptemplateForm()
    if request.method == "POST":
        desktoptemplatepost = DesktoptemplateForm(request.POST, files=request.FILES)
        if desktoptemplatepost.is_valid():
            desktoptemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('desktoptemplatepost')
    context={
        "desktoptemplatepost":desktoptemplatepost
    }
    return render(request, 'web/desktoptemplatepost.html',context)

@login_required(login_url='signin')
def microsofttemplatepost(request):
    microsofttemplatepost = MicrosofttemplateForm()
    if request.method == "POST":
        microsofttemplatepost = MicrosofttemplateForm(request.POST, files=request.FILES)
        if microsofttemplatepost.is_valid():
            microsofttemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('microsofttemplatepost')
    context={
        "microsofttemplatepost":microsofttemplatepost
    }
    return render(request, 'web/microsofttemplatepost.html',context)

@login_required(login_url='signin')
def adobeposttemplate(request):
    adobeposttemplate = AdobetemplateForm()
    if request.method == "POST":
        adobeposttemplate = AdobetemplateForm(request.POST, files=request.FILES)
        if adobeposttemplate.is_valid():
            adobeposttemplate.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('adobeposttemplate')
    context={
        "adobeposttemplate":adobeposttemplate
    }
    return render(request, 'web/adobeposttemplate.html',context)


class viewwebsite(DetailView):
    model = Website
    template_name = 'web/viewwebsite.html'
    comment_form_class = CommentwebsiteForm
    payment_form_class = PaymentWebsiteForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewwebsite", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentwebsite = PaymentWebsite.objects.create(
                    user=request.user,
                    website=self.object,
                    payment_status='pending',
                    amount=self.object.amount

                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentwebsite.unique_code)
                request.session['amount'] = f"{paymentwebsite.amount:.2f}"
                request.session['payment_type'] = "website"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentwebsite URL with required parameters
                return redirect(reverse('paymentwebsite', kwargs={
                    'course_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentwebsite.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentWebsite.objects.filter(user=self.request.user, website=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context

    
class viewmobile(DetailView):
    model = Mobile
    template_name = 'web/viewmobile.html'
    comment_form_class = CommentmobileForm
    payment_form_class = PaymentMobileForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewmobile", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentmobile = PaymentMobile.objects.create(
                    user=request.user,
                    mobile=self.object,
                    payment_status='pending',
                    amount=self.object.amount
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentmobile.unique_code)
                request.session['amount'] = f"{paymentmobile.amount:.2f}"
                request.session['payment_type'] = "mobile"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentmobile URL with required parameters
                return redirect(reverse('paymentmobile', kwargs={
                    'course_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentmobile.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentMobile.objects.filter(user=self.request.user, mobile=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context

    
class viewdesktop(DetailView):
    model = Desktop
    template_name = 'web/viewdesktop.html'
    comment_form_class = CommentdesktopForm
    payment_form_class = PaymentDesktopForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewdesktop", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentdesktop = PaymentDesktop.objects.create(
                    user=request.user,
                    desktop=self.object,
                    payment_status='pending',
                    amount=self.object.amount
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentdesktop.unique_code)
                request.session['amount'] = f"{paymentdesktop.amount:.2f}"
                request.session['payment_type'] = "desktop"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentdesktop URL with required parameters
                return redirect(reverse('paymentdesktop', kwargs={
                    'course_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentdesktop.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentDesktop.objects.filter(user=self.request.user, desktop=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context



class viewembeded(DetailView):
    model = Embeded
    template_name = 'web/viewembeded.html'
    comment_form_class = CommentembededForm
    payment_form_class = PaymentEmbededForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewembeded", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentembeded = PaymentEmbeded.objects.create(
                    user=request.user,
                    embeded=self.object,
                    payment_status='pending',
                    amount=self.object.amount
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentembeded.unique_code)
                request.session['amount'] = f"{paymentembeded.amount:.2f}"
                request.session['payment_type'] = "embeded"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentembeded URL with required parameters
                return redirect(reverse('paymentembeded', kwargs={
                    'course_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentembeded.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentEmbeded.objects.filter(user=self.request.user, embeded=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context



class viewgraphics(DetailView):
    model = Graphics
    template_name = 'web/viewgraphics.html'
    comment_form_class = CommentgraphicsForm
    payment_form_class = PaymentGraphicsForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewgraphics", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentgraphics = PaymentGraphics.objects.create(
                    user=request.user,
                    graphics=self.object,
                    payment_status='pending',
                    amount=self.object.amount
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentgraphics.unique_code)
                request.session['amount'] = f"{paymentgraphics.amount:.2f}"
                request.session['payment_type'] = "graphics"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentgraphics URL with required parameters
                return redirect(reverse('paymentgraphics', kwargs={
                    'course_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentgraphics.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentGraphics.objects.filter(user=self.request.user, graphics=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context


# VIEW FOR VIEWING PROJECT
class viewproject(DetailView):
    model = Project
    template_name = 'web/viewproject.html'
    comment_form_class = CommentprojectForm
    payment_form_class = PaymentProjectForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewproject", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentproject = PaymentProject.objects.create(
                    user=request.user,
                    project=self.object,
                    payment_status='pending',
                    amount=self.object.amount
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentproject.unique_code)
                request.session['amount'] = f"{paymentproject.amount:.2f}"
                request.session['payment_type'] = "project"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentproject URL with required parameters
                return redirect(reverse('paymentproject', kwargs={
                    'project_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentproject.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentProject.objects.filter(user=self.request.user, project=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context
    
# VIEW FOR VIEWING IMAGE
class viewimage(DetailView):
    model = Image
    template_name = 'web/viewimage.html'
    comment_form_class = CommentimageForm
    payment_form_class = PaymentImageForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewimage", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                paymentproject = PaymentImage.objects.create(
                    user=request.user,
                    image=self.object,
                    payment_status='pending',
                    amount=self.object.amount
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(paymentproject.unique_code)
                request.session['amount'] = f"{paymentproject.amount:.2f}"
                request.session['payment_type'] = "image"
                request.session['Title'] = slugify(self.object.Title)
                
                # Redirect to the paymentproject URL with required parameters
                return redirect(reverse('paymentimage', kwargs={
                    'image_id': self.object.id,
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentimage.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        
        # Get the payment status for the current user and website
        payment_status = None
        if self.request.user.is_authenticated:
            payment = PaymentImage.objects.filter(user=self.request.user, image=self.object).last()
            if payment:
                payment_status = payment.payment_status
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
            'payment_status': payment_status,
        })
        return context
    

@login_required(login_url='signin')
def viewwebsitetemplate(request, id):
    # Retrieve the website template
    websitetemplate = get_object_or_404(Websitetemplate, id=id)
    Websitetemplateview = Websitetemplate.objects.get(id=id)

    # Check if the user has made a payment for this template
    is_paid = False
    if request.user.is_authenticated:
        payment = Payment.objects.filter(user=request.user, template=websitetemplate).last()
        if payment and payment.payment_status == 'paid':
            is_paid = True
    
    context = {
        "Websitetemplateview":Websitetemplateview,
        'Websitetemplateview': websitetemplate,
        'is_paid': is_paid,
        }
    return render(request, 'web/viewwebsitetemplate.html', context)


@login_required(login_url='signin')
def viewmobiletemplate(request, id):
    mobiletemplate = get_object_or_404(Mobiletemplate, id=id)
    mobiletemplateview = Mobiletemplate.objects.get(id=id)
    
    # Check if the user has made a payment for this template
    is_paid = False
    if request.user.is_authenticated:
        payment = PaymentMobiletemplate.objects.filter(user=request.user, mobiletemplate=mobiletemplate).last()
        if payment and payment.payment_status == 'paid':
            is_paid = True
    
    context = {
        "mobiletemplateview":mobiletemplateview,
        'mobiletemplateview': mobiletemplateview,
        'is_paid': is_paid,
        }
    return render(request, 'web/viewmobiletemplate.html', context)


@login_required(login_url='signin')
def viewdesktoptemplate(request, id):
    desktoptemplate = get_object_or_404(Desktoptemplate, id=id)
    desktoptemplateview = Desktoptemplate.objects.get(id=id)
    
    # Check if the user has made a payment for this template
    is_paid = False
    if request.user.is_authenticated:
        payment = PaymentDesktoptemplate.objects.filter(user=request.user, desktoptemplate=desktoptemplate).last()
        if payment and payment.payment_status == 'paid':
            is_paid = True
    
    context = {
        "desktoptemplateview":desktoptemplateview,
        'desktoptemplateview': desktoptemplateview,
        'is_paid': is_paid,
        }
    return render(request, 'web/viewdesktoptemplate.html', context)

@login_required(login_url='signin')
def viewmicrosofttemplate(request, id):
     # Retrieve the microsoft template
    microsofttemplate = get_object_or_404(Microsofttemplate, id=id)
    microsofttemplateview = Microsofttemplate.objects.get(id=id)

    # Check if the user has made a payment for this template
    is_paid = False
    if request.user.is_authenticated:
        payment = PaymentMicrosofttemplate.objects.filter(user=request.user, microsofttemplate=microsofttemplate).last()
        if payment and payment.payment_status == 'paid':
            is_paid = True
    
    context = {
        "microsofttemplateview":microsofttemplateview,
        # 'microsofttemplate': microsofttemplate,
        'is_paid': is_paid,
        }
    return render(request, 'web/viewmicrosofttemplate.html', context)


@login_required(login_url='signin')
def viewadobetemplate(request, id):
     # Retrieve the adobe template
    adobetemplate = get_object_or_404(Adobetemplate, id=id)
    adobetemplateview = Adobetemplate.objects.get(id=id)

    # Check if the user has made a payment for this template
    is_paid = False
    if request.user.is_authenticated:
        payment = PaymentAdobetemplate.objects.filter(user=request.user, adobetemplate=adobetemplate).last()
        if payment and payment.payment_status == 'paid':
            is_paid = True
    
    context = {
        "adobetemplateview":adobetemplateview,
        # 'adobetemplate': adobetemplate,
        'is_paid': is_paid,
        }
    return render(request, 'web/viewadobetemplate.html', context)


# views for deleting the course
@login_required(login_url='signin')
def deletewebsite(request, id):
    websitedelete = Website.objects.get(id=id)
    if request.method == "POST":
        websitedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('website')
    
    context = {"websitedelete":websitedelete}
    return render(request, 'web/deletewebsite.html', context)

@login_required(login_url='signin')
def deletemobile(request, id):
    mobiledelete = Mobile.objects.get(id=id)
    if request.method == "POST":
        mobiledelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('mobileapp')
    
    context = {"mobiledelete":mobiledelete}
    return render(request, 'web/deletemobile.html', context)

@login_required(login_url='signin')
def deletedesktop(request, id):
    desktopdelete = Desktop.objects.get(id=id)
    if request.method == "POST":
        desktopdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('desktopapp')
    
    context = {"desktopdelete":desktopdelete}
    return render(request, 'web/deletedesktop.html', context)

@login_required(login_url='signin')
def deleteembeded(request, id):
    embededdelete = Embeded.objects.get(id=id)
    if request.method == "POST":
        embededdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('embeded')
    
    context = {"embededdelete":embededdelete}
    return render(request, 'web/deleteembeded.html', context)

@login_required(login_url='signin')
def deletegraphics(request, id):
    graphicsdelete = Graphics.objects.get(id=id)
    if request.method == "POST":
        graphicsdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('graphics')
    
    context = {"graphicsdelete":graphicsdelete}
    return render(request, 'web/deletegraphics.html', context)

# DELETING PROJECT
@login_required(login_url='signin')
def deleteproject(request, id):
    projectdelete = Project.objects.get(id=id)
    if request.method == "POST":
        projectdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('graphics')
    
    context = {"projectdelete":projectdelete}
    return render(request, 'web/deleteproject.html', context)

# DELETING IMAGE
@login_required(login_url='signin')
def deleteimage(request, id):
    imagedelete = Image.objects.get(id=id)
    if request.method == "POST":
        imagedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('image')
    
    context = {"imagedelete":imagedelete}
    return render(request, 'web/deleteimage.html', context)

# views for deleting template
@login_required(login_url='signin')
def deletewebsitetemplate(request, id):
    Website = Websitetemplate.objects.get(id=id)
    if request.method == "POST":
        Website.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('Website')
    
    context = {"Website":Website}
    return render(request, 'web/deletewebsitetemplate.html', context)

@login_required(login_url='signin')
def deletemobiletemplate(request, id):
    mobiletemplatedelete = Mobiletemplate.objects.get(id=id)
    if request.method == "POST":
        mobiletemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('mobiletemplate')
    
    context = {"mobiletemplatedelete":mobiletemplatedelete}
    return render(request, 'web/deletemobiletemplate.html', context)

@login_required(login_url='signin')
def deletedesktoptemplate(request, id):
    desktoptemplatedelete = Desktoptemplate.objects.get(id=id)
    if request.method == "POST":
        desktoptemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('desktoptemplate')
    
    context = {"desktoptemplatedelete":desktoptemplatedelete}
    return render(request, 'web/deletedesktoptemplate.html', context)

@login_required(login_url='signin')
def deletemicrosofttemplate(request, id):
    microsofttemplatedelete = Microsofttemplate.objects.get(id=id)
    if request.method == "POST":
        microsofttemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('microsofttemplate')
    
    context = {"microsofttemplatedelete":microsofttemplatedelete}
    return render(request, 'web/deletemicrosofttemplate.html', context)

@login_required(login_url='signin')
def deleteadobetemplate(request, id):
    adobetemplatedelete = Adobetemplate.objects.get(id=id)
    if request.method == "POST":
        adobetemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('adobetemplate')
    
    context = {"adobetemplatedelete":adobetemplatedelete}
    return render(request, 'web/deleteadobetemplate.html', context)


# views for the updating course and templates
@login_required(login_url='signin')
def updatewebsite(request, id):
    a = Website.objects.get(id=id)
    website = WebsiteForm(instance=a)
    if request.method == "POST":
        website = WebsiteForm(request.POST, files=request.FILES, instance=a)
        if website.is_valid():
            website.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('website')
    context = {"website":website}
    return render(request, 'web/updatewebsite.html', context)

@login_required(login_url='signin')
def updatemobile(request, id):
    b = Mobile.objects.get(id=id)
    mobile = MobileForm(instance=b)
    if request.method == "POST":
        mobile = MobileForm(request.POST, files=request.FILES, instance=b)
        if mobile.is_valid():
            mobile.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('mobileapp')
    context = {"mobile":mobile}
    return render(request, 'web/updatemobile.html', context)

@login_required(login_url='signin')
def updatedesktop(request, id):
    c = Desktop.objects.get(id=id)
    desktop = DesktopForm(instance=c)
    if request.method == "POST":
        desktop = DesktopForm(request.POST, files=request.FILES, instance=c)
        if desktop.is_valid():
            desktop.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('desktopapp')
    context = {"desktop":desktop}
    return render(request, 'web/updatedesktop.html', context)

@login_required(login_url='signin')
def updateembeded(request, id):
    d = Embeded.objects.get(id=id)
    embeded = EmbededForm(instance=d)
    if request.method == "POST":
        embeded = EmbededForm(request.POST, files=request.FILES, instance=d)
        if embeded.is_valid():
            embeded.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('embeded')
    context = {"embeded":embeded}
    return render(request, 'web/updateembeded.html', context)

@login_required(login_url='signin')
def updategraphics(request, id):
    j = Graphics.objects.get(id=id)
    graphics = GraphicsForm(instance=j)
    if request.method == "POST":
        graphics = GraphicsForm(request.POST, files=request.FILES, instance=j)
        if graphics.is_valid():
            graphics.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('graphics')
    context = {"graphics":graphics}
    return render(request, 'web/updategraphics.html', context)


# FOR UPDATING PROJECT
@login_required(login_url='signin')
def updateproject(request, id):
    n = Project.objects.get(id=id)
    project = ProjectForm(instance=n)
    if request.method == "POST":
        project = ProjectForm(request.POST, files=request.FILES, instance=n)
        if project.is_valid():
            project.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('websiteproject')
    context = {"project":project}
    return render(request, 'web/updateproject.html', context)

# FOR UPDATING IMAGE
@login_required(login_url='signin')
def updateimage(request, id):
    q = Image.objects.get(id=id)
    image = ImageForm(instance=q)
    if request.method == "POST":
        image = ImageForm(request.POST, files=request.FILES, instance=q)
        if image.is_valid():
            image.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('image')
    context = {"image":image}
    return render(request, 'web/updateimage.html', context)


# views for updating template
@login_required(login_url='signin')
def updatewebsitetemplate(request, id):
    e = Websitetemplate.objects.get(id=id)
    websitetemplate = WebsitetemplateForm(instance=e)
    if request.method == "POST":
        websitetemplate = WebsitetemplateForm(request.POST, files=request.FILES, instance=e)
        if websitetemplate.is_valid():
            websitetemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('websitetemplate')
    context = {"websitetemplate":websitetemplate}
    return render(request, 'web/updatewebsitetemplate.html', context)

@login_required(login_url='signin')
def updatemobiletemplate(request, id):
    f = Mobiletemplate.objects.get(id=id)
    mobiletemplate = MobiletetemplateForm(instance=f)
    if request.method == "POST":
        mobiletemplate = MobiletetemplateForm(request.POST, files=request.FILES, instance=f)
        if mobiletemplate.is_valid():
            mobiletemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('mobiletemplate')
    context = {"mobiletemplate":mobiletemplate}
    return render(request, 'web/updatemobiletemplate.html', context)

@login_required(login_url='signin')
def updatedesktoptemplate(request, id):
    g = Desktoptemplate.objects.get(id=id)
    desktoptemplate = DesktoptemplateForm(instance=g)
    if request.method == "POST":
        desktoptemplate = DesktoptemplateForm(request.POST, files=request.FILES, instance=g)
        if desktoptemplate.is_valid():
            desktoptemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('desktoptemplate')
    context = {"desktoptemplate":desktoptemplate}
    return render(request, 'web/updatedesktoptemplate.html', context)

@login_required(login_url='signin')
def updatemicrosofttemplate(request, id):
    h = Microsofttemplate.objects.get(id=id)
    microsofttemplate = MicrosofttemplateForm(instance=h)
    if request.method == "POST":
        microsofttemplate = MicrosofttemplateForm(request.POST, files=request.FILES, instance=h)
        if microsofttemplate.is_valid():
            microsofttemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('microsofttemplate')
    context = {"microsofttemplate":microsofttemplate}
    return render(request, 'web/updatemicrosofttemplate.html', context)

@login_required(login_url='signin')
def updateadobetemplate(request, id):
    i = Adobetemplate.objects.get(id=id)
    adobeposttemplate = AdobetemplateForm(instance=i)
    if request.method == "POST":
        adobeposttemplate = AdobetemplateForm(request.POST, files=request.FILES, instance=i)
        if adobeposttemplate.is_valid():
            adobeposttemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('adobeposttemplate')
    context = {"adobeposttemplate":adobeposttemplate}
    return render(request, 'web/updateadobetemplate.html', context)


 
 # FOR PAYMENT OF TEMPLATES
class PaymentViewWebsitetemplate(LoginRequiredMixin, View, PaymentRequestMixin):
    template_name = "web/payment.html"

    def get(self, request, id):
        template = get_object_or_404(Websitetemplate, id=id)
        payment = Payment.objects.create(
            user=request.user,
            template=template,
            payment_status='pending',
            amount=template.amount
        )
        request.session['unique_code'] = payment.unique_code
        request.session['payment_type'] = "websitetemplate"
        order_info = {
            "amount": template.amount,
            "description": f"Payment for {template.Title}",
            "reference": payment.id,
            "email": request.user.email,
        }
        pesapal_url = self.get_payment_url(**order_info)
        return render(request, self.template_name, {'pesapal_url': pesapal_url})

class PaymentViewMobiletemplate(LoginRequiredMixin, View, PaymentRequestMixin):
    template_name = "web/payment.html"

    def get(self, request, id):
        mobiletemplate = get_object_or_404(Mobiletemplate, id=id)
        mobiletemplatepayment = PaymentMobiletemplate.objects.create(
            user=request.user,
            mobiletemplate=mobiletemplate,
            payment_status='pending',
            amount=mobiletemplate.amount
        )
        request.session['unique_code'] = mobiletemplatepayment.unique_code
        request.session['payment_type'] = "mobiletemplate"
        order_info = {
            "amount": mobiletemplate.amount,
            "description": f"Payment for {mobiletemplate.Title}",
            "reference": mobiletemplatepayment.id,
            "email": request.user.email,
        }
        pesapal_url = self.get_payment_url(**order_info)
        return render(request, self.template_name, {'pesapal_url': pesapal_url})

class PaymentViewDesktoptemplate(LoginRequiredMixin, View, PaymentRequestMixin):
    template_name = "web/payment.html"

    def get(self, request, id):
        desktoptemplate = get_object_or_404(Desktoptemplate, id=id)
        desktoptemplatepayment = PaymentDesktoptemplate.objects.create(
            user=request.user,
            desktoptemplate=desktoptemplate,
            payment_status='pending',
            amount=desktoptemplate.amount
        )
        request.session['unique_code'] = desktoptemplatepayment.unique_code
        request.session['payment_type'] = "desktoptemplate"
        order_info = {
            "amount": desktoptemplate.amount,
            "description": f"Payment for {desktoptemplate.Title}",
            "reference": desktoptemplatepayment.id,
            "email": request.user.email,
        }
        pesapal_url = self.get_payment_url(**order_info)
        return render(request, self.template_name, {'pesapal_url': pesapal_url})
    
class PaymentViewMicrosofttemplate(LoginRequiredMixin, View, PaymentRequestMixin):
    template_name = "web/payment.html"

    def get(self, request, id):
        microsofttemplate = get_object_or_404(Microsofttemplate, id=id)
        microsofttemplatepayment = PaymentMicrosofttemplate.objects.create(
            user=request.user,
            microsofttemplate=microsofttemplate,
            payment_status='pending',
            amount=microsofttemplate.amount
        )
        request.session['unique_code'] = microsofttemplatepayment.unique_code
        request.session['payment_type'] = "microsofttemplate"
        order_info = {
            "amount": microsofttemplate.amount,
            "description": f"Payment for {microsofttemplate.Title}",
            "reference": microsofttemplatepayment.id,
            "email": request.user.email,
        }
        pesapal_url = self.get_payment_url(**order_info)
        return render(request, self.template_name, {'pesapal_url': pesapal_url})
    
class PaymentViewAdobetemplate(LoginRequiredMixin, View, PaymentRequestMixin):
    template_name = "web/payment.html"

    def get(self, request, id):
        adobetemplate = get_object_or_404(Adobetemplate, id=id)
        adobetemplatepayment = PaymentAdobetemplate.objects.create(
            user=request.user,
            adobetemplate=adobetemplate,
            payment_status='pending',
            amount=adobetemplate.amount
        )
        request.session['unique_code'] = adobetemplatepayment.unique_code
        request.session['payment_type'] = "adobetemplate"
        order_info = {
            "amount": adobetemplate.amount,
            "description": f"Payment for {adobetemplate.Title}",
            "reference": adobetemplatepayment.id,
            "email": request.user.email,
        }
        pesapal_url = self.get_payment_url(**order_info)
        return render(request, self.template_name, {'pesapal_url': pesapal_url})



 # FOR PAYMENT OF COURSES 
class PaymentViewWebsite(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, course_id):
        # website = get_object_or_404(Website, id=id)
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'course_id': course_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['course_id'] = course_id
        request.session['payment_type'] = "website"
        # request.session['website'] = website

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": course_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})


    
class PaymentViewMobile(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, course_id):
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'course_id': course_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['course_id'] = course_id
        request.session['payment_type'] = "mobile"

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": course_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})


    
class PaymentViewDesktop(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, course_id):
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'course_id': course_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['course_id'] = course_id
        request.session['payment_type'] = "desktop"

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": course_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})


class PaymentViewEmbeded(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, course_id):
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'course_id': course_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['course_id'] = course_id
        request.session['payment_type'] = "embeded"

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": course_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})

    
class PaymentViewGraphics(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, course_id):
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'course_id': course_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['course_id'] = course_id
        request.session['payment_type'] = "graphics"

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": course_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})

 # VIEWS FOR PROJECT PAYMENT
class PaymentViewProject(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, project_id):
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'project_id': project_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['project_id'] = project_id
        request.session['payment_type'] = "project"

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": project_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url}) 


# VIEWS FOR PROJECT PAYMENT
class PaymentViewImage(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, image_id):
        unique_code = request.session.get('unique_code')
        Title = request.session.get('Title')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'image_id': image_id,
        }

        # Store the data in the session
        request.session['unique_code'] = unique_code
        request.session['image_id'] = image_id
        request.session['payment_type'] = "image"

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {Title}",
            "reference": image_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})
    
    
# UPDATING PAYMENT
def update_websitetemplatepayment_status(payment, transaction_id):
    """Update the payment status to 'paid'."""
    payment.payment_status = 'paid'
    payment.transaction_id = transaction_id
    payment.save()
    
def update_mobiletemplatepayment_status(mobiletemplatepayment, transaction_id):
    """Update the payment status to 'paid'."""
    mobiletemplatepayment.payment_status = 'paid'
    mobiletemplatepayment.transaction_id = transaction_id
    mobiletemplatepayment.save()
    
def update_desktoptemplatepayment_status(desktoptemplatepayment, transaction_id):
    """Update the payment status to 'paid'."""
    desktoptemplatepayment.payment_status = 'paid'
    desktoptemplatepayment.transaction_id = transaction_id
    desktoptemplatepayment.save()
    
def update_microsofttemplatepayment_status(microsofttemplatepayment, transaction_id):
    """Update the payment status to 'paid'."""
    microsofttemplatepayment.payment_status = 'paid'
    microsofttemplatepayment.transaction_id = transaction_id
    microsofttemplatepayment.save()
    
def update_adobetemplatepayment_status(adobetemplatepayment, transaction_id):
    """Update the payment status to 'paid'."""
    adobetemplatepayment.payment_status = 'paid'
    adobetemplatepayment.transaction_id = transaction_id
    adobetemplatepayment.save()
    
# UPDATING PAYMENT FOR COURSES
def update_websitepayment_status(websitepayment, transaction_id):
    """Update the payment status to 'paid'."""
    websitepayment.payment_status = 'paid'
    websitepayment.transaction_id = transaction_id
    websitepayment.save()
    
def update_mobilepayment_status(mobilepayment, transaction_id):
    """Update the payment status to 'paid'."""
    mobilepayment.payment_status = 'paid'
    mobilepayment.transaction_id = transaction_id
    mobilepayment.save()
    
def update_desktoppayment_status(desktoppayment, transaction_id):
    """Update the payment status to 'paid'."""
    desktoppayment.payment_status = 'paid'
    desktoppayment.transaction_id = transaction_id
    desktoppayment.save()
    
def update_embededpayment_status(embededpayment, transaction_id):
    """Update the payment status to 'paid'."""
    embededpayment.payment_status = 'paid'
    embededpayment.transaction_id = transaction_id
    embededpayment.save()
    
def update_graphicspayment_status(graphicspayment, transaction_id):
    """Update the payment status to 'paid'."""
    graphicspayment.payment_status = 'paid'
    graphicspayment.transaction_id = transaction_id
    graphicspayment.save()

# UPDATE PAYMENT FOR PROJECT
def update_projectpayment_status(projectpayment, transaction_id):
    """Update the payment status to 'paid'."""
    projectpayment.payment_status = 'paid'
    projectpayment.transaction_id = transaction_id
    projectpayment.save()
    
# UPDATE PAYMENT FOR IMAGE
def update_imagepayment_status(imagepayment, transaction_id):
    """Update the payment status to 'paid'."""
    imagepayment.payment_status = 'paid'
    imagepayment.transaction_id = transaction_id
    imagepayment.save()
    
    
#HANDLING PAYMENT
def handle_websitetemplate_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    payment = Payment.objects.filter(user=request.user).last()
    if payment:
        template_id = payment.template.id
        payment = get_object_or_404(Payment, template_id=template_id, unique_code=unique_code, user=request.user)
        update_websitetemplatepayment_status(payment, transaction_id)
        return redirect(reverse('viewwebsitetemplate', args=[template_id]))
    return None

def handle_mobiletemplate_payment(request, transaction_id, unique_code):
    """Handle mobile template payment."""
    mobiletemplatepayment = PaymentMobiletemplate.objects.filter(user=request.user).last()
    if mobiletemplatepayment:
        mobiletemplate_id = mobiletemplatepayment.mobiletemplate.id
        mobiletemplatepayment = get_object_or_404(PaymentMobiletemplate, mobiletemplate_id=mobiletemplate_id, unique_code=unique_code, user=request.user)
        update_mobiletemplatepayment_status(mobiletemplatepayment, transaction_id)
        return redirect(reverse('viewmobiletemplate', args=[mobiletemplate_id]))
    return None

def handle_desktoptemplate_payment(request, transaction_id, unique_code):
    """Handle desktop template payment."""
    desktoptemplatepayment = PaymentDesktoptemplate.objects.filter(user=request.user).last()
    if desktoptemplatepayment:
        desktoptemplate_id = desktoptemplatepayment.desktoptemplate.id
        desktoptemplatepayment = get_object_or_404(PaymentDesktoptemplate, desktoptemplate_id=desktoptemplate_id, unique_code=unique_code, user=request.user)
        update_desktoptemplatepayment_status(desktoptemplatepayment, transaction_id)
        return redirect(reverse('viewdesktoptemplate', args=[desktoptemplate_id]))
    return None

def handle_microsofttemplate_payment(request, transaction_id, unique_code):
    """Handle mobile template payment."""
    microsofttemplatepayment = PaymentMicrosofttemplate.objects.filter(user=request.user).last()
    if microsofttemplatepayment:
        microsofttemplate_id = mobiletemplatepayment.mobiletemplate.id
        mobiletemplatepayment = get_object_or_404(PaymentMicrosofttemplate, microsofttemplate_id=microsofttemplate_id, unique_code=unique_code, user=request.user)
        update_microsofttemplatepayment_status(microsofttemplatepayment, transaction_id)
        return redirect(reverse('viewmobiletemplate', args=[microsofttemplate_id]))
    return None

def handle_adobetemplate_payment(request, transaction_id, unique_code):
    """Handle desktop template payment."""
    adobetemplatepayment = PaymentAdobetemplate.objects.filter(user=request.user).last()
    if adobetemplatepayment:
        adobetemplate_id = adobetemplatepayment.adobetemplate.id
        adobetemplatepayment = get_object_or_404(PaymentAdobetemplate, adobetemplate_id=adobetemplate_id, unique_code=unique_code, user=request.user)
        update_adobetemplatepayment_status(adobetemplatepayment, transaction_id)
        return redirect(reverse('viewadobetemplate', args=[adobetemplate_id]))
    return None

#HANDLING PAYMENT FOR COURSES
def handle_website_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    websitepayment = PaymentWebsite.objects.filter(user=request.user).last()
    course_id = request.session.get('course_id')
    if websitepayment:
        websitepayment = get_object_or_404(PaymentWebsite,unique_code=unique_code, user=request.user)
        update_websitepayment_status(websitepayment, transaction_id)
        return redirect(reverse('viewwebsite', args=[course_id]))
    return None

def handle_mobile_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    mobilepayment = PaymentMobile.objects.filter(user=request.user).last()
    course_id = request.session.get('course_id')
    if mobilepayment:
        mobilepayment = get_object_or_404(PaymentMobile, unique_code=unique_code, user=request.user)
        update_mobilepayment_status(mobilepayment, transaction_id)
        return redirect(reverse('viewmobile', args=[course_id]))
    return None


def handle_desktop_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    desktoppayment = PaymentDesktop.objects.filter(user=request.user).last()
    course_id = request.session.get('course_id')
    if desktoppayment:
        desktoppayment = get_object_or_404(PaymentDesktop, unique_code=unique_code, user=request.user)
        update_desktoppayment_status(desktoppayment, transaction_id)
        return redirect(reverse('viewdesktop', args=[course_id]))
    return None

def handle_embeded_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    embededpayment = PaymentEmbeded.objects.filter(user=request.user).last()
    course_id = request.session.get('course_id')
    if embededpayment:
        embededpayment = get_object_or_404(PaymentEmbeded, unique_code=unique_code, user=request.user)
        update_embededpayment_status(embededpayment, transaction_id)
        return redirect(reverse('viewembeded', args=[course_id]))
    return None

def handle_graphics_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    graphicspayment = PaymentGraphics.objects.filter(user=request.user).last()
    course_id = request.session.get('course_id')
    if graphicspayment:
        graphicspayment = get_object_or_404(PaymentGraphics, unique_code=unique_code, user=request.user)
        update_graphicspayment_status(graphicspayment, transaction_id)
        return redirect(reverse('viewgraphics', args=[course_id]))
    return None

# HANDLE PAYMENT FOR PROJECT
def handle_project_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    projectpayment = PaymentProject.objects.filter(user=request.user).last()
    project_id = request.session.get('project_id')
    if projectpayment:
        projectpayment = get_object_or_404(PaymentProject, unique_code=unique_code, user=request.user)
        update_projectpayment_status(projectpayment, transaction_id)
        return redirect(reverse('viewproject', args=[project_id]))
    return None

# HANDLE PAYMENT FOR IMAGE
def handle_image_payment(request, transaction_id, unique_code):
    """Handle website template payment."""
    imagepayment = PaymentImage.objects.filter(user=request.user).last()
    image_id = request.session.get('image_id')
    if imagepayment:
        imagepayment = get_object_or_404(PaymentImage, unique_code=unique_code, user=request.user)
        update_imagepayment_status(imagepayment, transaction_id)
        return redirect(reverse('viewimage', args=[image_id]))
    return None

# PAYMENT COMPLETION
def payment_completed(request):
    transaction_id = request.GET.get('pesapal_transaction_tracking_id')
    unique_code = request.session.get('unique_code')
    payment_type = request.session.get('payment_type')
    website = request.session.get('website')
    course_id = request.session.get('course_id')
    project_id = request.session.get('project_id')
    image_id = request.session.get('image_id')
    
    
    request.session['course_id'] = course_id
    request.session['project_id'] = project_id
    request.session['image_id'] = image_id

    if payment_type == 'websitetemplate':
        response = handle_websitetemplate_payment(request, transaction_id, unique_code)
    elif payment_type == 'mobiletemplate':
        response = handle_mobiletemplate_payment(request, transaction_id, unique_code)
    elif payment_type == 'desktoptemplate':
        response = handle_desktoptemplate_payment(request, transaction_id, unique_code)
    elif payment_type == 'microsofttemplate':
        response = handle_microsofttemplate_payment(request, transaction_id, unique_code)
    elif payment_type == 'adobetemplate':
        response = handle_adobetemplate_payment(request, transaction_id, unique_code)
    elif payment_type == 'website':
        response = handle_website_payment(request, transaction_id, unique_code)
    elif payment_type == 'mobile':
        response = handle_mobile_payment(request, transaction_id, unique_code)
    elif payment_type == 'desktop':
        response = handle_desktop_payment(request, transaction_id, unique_code)
    elif payment_type == 'embeded':
        response = handle_embeded_payment(request, transaction_id, unique_code)
    elif payment_type == 'graphics':
        response = handle_graphics_payment(request, transaction_id, unique_code)
    elif payment_type == 'project':
        response = handle_project_payment(request, transaction_id, unique_code)
    elif payment_type == 'image':
        response = handle_image_payment(request, transaction_id, unique_code)
    else:
        return redirect('website')  # Or any other appropriate view
    
    return response if response else redirect('websitetemplate')


