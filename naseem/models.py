from django.db import models

from django.contrib.auth.models import User


class Attendance(models.Model):
	StudentName=models.CharField(max_length=200,null=True)
	StudentId=models.CharField(max_length=50,blank=True,null=True)
	LectureAttend=models.IntegerField(blank=True,null=True)
	TotalLectures=models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.StudentName



class Marks(models.Model):
	StudentName=models.CharField(max_length=200,blank=True,null=True)
	StudentId=models.CharField(max_length=50,blank=True,null=True)
	PhysicsMarks=models.IntegerField(blank=True,null=True)
	ChemistryMarks=models.IntegerField(null=True)
	EnglishMarks=models.IntegerField(blank=True,null=True)
	MathsMarks=models.IntegerField(blank=True,null=True)
	ComputerMarks=models.IntegerField(blank=True,null=True)


	def __str__(self):
		return self.StudentName


class Notice(models.Model):
	Message=models.CharField(max_length=200,null=True)
	date_created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.Message



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def extension(self):
    	description, extension = os.path.splitext(self.document.description)
    	return extension


   