
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 
class addAttendanceform(ModelForm):
    class Meta:
        model=Attendance
        fields="__all__"
 
class addMarksform(ModelForm):
    class Meta:
        model=Marks
        fields="__all__"
 
class addNoticeform(ModelForm):
    class Meta:
        model=Notice
        fields="__all__"

 
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )