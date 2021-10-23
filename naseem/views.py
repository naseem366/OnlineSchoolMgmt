from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			name=request.POST['name']
			username=request.POST['username']
			email=request.POST['email']
			password1=request.POST['password1']
			password2=request.POST['password2']

			if password1==password2:
				if User.objects.filter(username=username).exists():
					messages.info(request,'username is taken')
					return redirect('login')
				elif User.objects.filter(email=email).exists():
					messages.info(request,'email already taken')
					return redirect('login')
				else:
					user=User.objects.create_user(first_name=name,username=username,email=email,password=password1)
					user.save()
					return redirect('login')
			else:
				messages.info(request,"password not maching ")
				return redirect('login')
			return redirect('/')
		else:
			return render(request,'Register.html')



	return render(request,'Register.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method=='POST':
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('/')
			else:
				messages.info(request,'Invalide credential')
				context={}
				return render(request,'Login.html',context)
		else:
			return render(request,'Login.html')  

def logoutPage(request):
	logout(request)
	return redirect('login')
	
 
def home(request):
	if request.user.is_authenticated:
		notice=Notice.objects.all()
		attendance=Attendance.objects.all()
		marks=Marks.objects.all()
		documents=Document.objects.all()
		context={

			'notice':notice,
			'marks':marks,
			'attendance':attendance,
			'documents':documents,
		}
		return render(request,'Home.html',context)
	else:
		return redirect('login')

def addAttendance(request):
	if request.user.is_authenticated:
		form=addAttendanceform()
		if request.method == 'POST':
			form=addAttendanceform(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')
		context={'form':form}
		return render(request,'AddAttendance.html',context)
	else:
		return redirect('home')

def addMarks(request):
	if request.user.is_authenticated:
		form=addMarksform()
		if request.method =='POST':
			form=addMarksform(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')
		context={'form':form}
		return render(request,'AddMarks.html',context)
	else:
		return redirect('home')

def addNotice(request):
	if request.user.is_authenticated:
		form=addNoticeform()
		if request.method == 'POST':
			form=addNoticeform(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')
		context={'form':form}
		return render(request,'AddNotice.html',context)
	else:
		return redirect('home')



def uploadPage(request):
	if request.user.is_authenticated:
		form=DocumentForm()
		if request.method == 'POST':
			form=DocumentForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return redirect('/')

		context={'form':form}
		return render(request,'upload.html',context)

	else:
		return redirect('home')


import os

from django.conf import settings

ROOT_PATH = os.path.split(os.path.abspath(__file__))[0]

def read_from_database(request):
    f = open(os.path.join(settings.ROOT_PATH, 'myfile.db'))




from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import BaseDetailView

class DisplayPdfView(BaseDetailView):
    def get(self, request, *args, **kwargs):
        objkey = self.kwargs.get('pk', None) #1
        pdf = get_object_or_404(pdf, pk=objkey) #2
        fname = pdf.filename() #3
        path = os.path.join(settings.MEDIA_ROOT, 'docs\\' + fname)#4
        response = FileResponse(open(path, 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename={}".format(fname)
        return response


import re, os
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

def resume1(request, applicant_id):

    #Get the applicant's resume
    resume = Document.objects.get(pk=applicant_id)
    fsock = open(resume.document,'r')
    response = HttpResponse(fsock, content_type='application/pdf')

    #filepath = os.path.join('static', 'sample.pdf')
    #response=FileResponse(open(fsock, 'rb'), content_type='application/pdf')

    return response


from django.http import FileResponse, Http404

def pdf_view22(request):
    try:
        return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def export_auto_doc(request):
    name = request.GET.get('name', "")
    filename = "path/to/file"+name+".pdf"
    try:
        if not re.search("^[a-zA-Z0-9]+$",name):
            raise ValueError("Filename wrong format")
        elif not os.path.isfile(filename):
            raise ValueError("Filename doesn't exist")
        else:
            with open(filename, 'r') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename='+name+'.pdf'
                return response
            pdf.closed
    except ValueError as e:
        str(e)
        return response

def pdf_view(request):
	#filepath=os.path.join('media_cdn/documents')
	#print(filepath)
	fd = os.path.join(settings.MEDIA_ROOT,'documents')
	filename="fd"+download+".pdf"
	try:
		if not re.search("^[a-zA-Z0-9]+$", filename):

			raise ValueError("Filename wrong format")
		elif not os.path.isfile(filename):
			raise ValueError("Filename doesn't exist")
		else:
			with open(filename,'r') as pdf:
				response = HttpResponse(pdf.read(), content_type='application/pdf')
            	response['Content-Disposition'] = 'inline;filename='+name+'.pdf'
            	return response
        	pdf.closed
    except ValueError as e:
    	str(e)
    	return response


	print(fd)
	
	if fd.endswith(".pdf"):
		print("hello")
	else:
		print("files does not exists")


from django.http import FileResponse
import os
 
def resume(request,applicant_id):

	resume = Document.objects.get(pk=applicant_id)
	print(resume)
	filepath=os.path.join('media_cdn/documents')
	print(filepath)
	extension = os.path.splitext(filepath)[1]
	print(extension)
	
	#return FileResponse(open(resume.document,'rb'),content_type='application/pdf')
    

import os.path
#extension = os.path.splitext(filename)[1]