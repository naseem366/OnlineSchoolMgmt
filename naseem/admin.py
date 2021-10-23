from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Attendance)
class AttendAdmin(admin.ModelAdmin):
	list_display=['StudentId','StudentName','LectureAttend','TotalLectures']

@admin.register(Marks)
class MarkAdmin(admin.ModelAdmin):
	list_display=['StudentId','StudentName','ComputerMarks','ChemistryMarks','MathsMarks','EnglishMarks','PhysicsMarks']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
	list_display=['Message','date_created']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	list_display=['id','description','document','uploaded_at']