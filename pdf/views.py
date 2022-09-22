from doctest import REPORT_CDIFF
from unicodedata import name
from urllib import response
from django.shortcuts import render,redirect
from .models import Profile
from django.http import HttpResponse
from django.template import Template
import io
from pdf.utils import render_to_pdf
# Create your views here.
def dashboard(request):
        if request.method == 'POST':
            #basic
            name=request.POST['name']
            lname=request.POST['lname']
            phone=request.POST['phone']
            email=request.POST['email']
            #address
            address1=request.POST['address1']
            address2=request.POST['address2']
            city=request.POST['city']
            state=request.POST['state']
            zip=request.POST['zip']
            #education
            school=request.POST['school']
            schoolclass=request.POST['schoolclass']
            schooly1=request.POST['schooly1']
            schooly2=request.POST['schooly2']

            degree=request.POST['degree']
            university=request.POST['university']
            degreein=request.POST['degreein']
            collegey1=request.POST['collegey1']
            collegey2=request.POST['collegey2']
            #about
            designation=request.POST['designation']
            about=request.POST['about']
            skill=request.POST['skill']
            profile = Profile(
                #basic
                name=name,lname=lname,phone=phone,email=email,
                #address
                address1=address1,address2=address2,city=city,state=state,zip=zip,
                #education
                school=school,schoolclass=schoolclass,schooly1=schooly1,schooly2=schooly2,
                degree=degree,university=university,degreein=degreein,collegey1=collegey1,collegey2=collegey2,
                #about
                designation=designation,about=about,skill=skill
                )
            profile.save()
        return render(request, 'accept.html')
def resume(request,id):
    user_profile=Profile.objects.get(pk = id)
    return render (request,'resume.html', {'user_profile':user_profile})
    
def download(request,id):
    user_profile=Profile.objects.get(pk = id)
    pdf = render_to_pdf('resume.html', {'user_profile':user_profile})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "%s_resume.pdf" % (user_profile.name)
        content = "inline; filename=%s"%(filename)
        content = "attachment; filename=%s"%(filename)
        response ['Content-Disposition'] = content
        return response
    return HttpResponse('Not found')
def list(request):
    profile = Profile.objects.all()
    return render (request, 'list.html',{'profile':profile})