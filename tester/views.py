
from importlib.resources import path
from django.views.generic import ListView
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Profile
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
import pdfkit


class profile_name1(ListView):
    model= Profile
    template_name= 'list1.html'

class profile_name2(ListView):
    model= Profile
    template_name= 'list2.html'

def dashboard(request):
        if request.method == 'POST':
            #basic
            profileimg = request.FILES['profileimg']
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
            stream = request.POST['stream']
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
                profileimg=profileimg,name=name,lname=lname,phone=phone,email=email,
                #address
                address1=address1,address2=address2,city=city,state=state,zip=zip,
                #education
                school=school,schoolclass=schoolclass,schooly1=schooly1,schooly2=schooly2,
                degree=degree,stream=stream,university=university,degreein=degreein,collegey1=collegey1,collegey2=collegey2,
                #about
                designation=designation,about=about,skill=skill
                )
            profile.save()
        return render(request, 'accept.html')


def pdflist(request,*args, **kwargs):
    return render(request, 'pdflist.html')



#render view template 1
def render_view_download1(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user_profile=Profile.objects.get(pk = pk)

    filename = user_profile.name
    template_path = 'resume.html'
    context = {'profile': user_profile}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)
    #response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it
    # create a pdf
    response['Content-Disposition'] = 'attachment; filename="{}_RESUME.pdf"'.format(filename.upper())
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
def render_pdf_view1(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user_profile=Profile.objects.get(pk = pk)
    filename = user_profile.name
    template_path = 'resume.html'
    context = {'profile': user_profile}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="{}_RESUME.pdf"'.format(filename.upper())
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#render view template 2
def render_view_download2(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user_profile=Profile.objects.get(pk = pk)

    filename = user_profile.name
    template_path = 'resume2.html'
    context = {'profile': user_profile}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)
    #response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it
    # create a pdf
    response['Content-Disposition'] = 'attachment; filename="{}_RESUME.pdf"'.format(filename.upper())
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
def render_pdf_view2(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user_profile=Profile.objects.get(pk = pk)
    filename = user_profile.name
    template_path = 'resume2.html'
    context = {'profile': user_profile}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="{}_RESUME.pdf"'.format(filename.upper())
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
