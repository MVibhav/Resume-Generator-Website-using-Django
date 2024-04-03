from django.db import models

class EducationDetails(models.Model):
    school=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    startdate=models.DateField()
    enddate=models.DateField()
    city=models.CharField(max_length=200)
    percent=models.CharField(max_length=200)

class EmployeeDetails(models.Model):
    jobtitle=models.CharField(max_length=200)
    employer=models.CharField(max_length=200)
    startdate=models.DateField()
    enddate=models.DateField()
    city=models.CharField(max_length=200)
    description=models.TextField(max_length=2500)

class Skill(models.Model):
    skill=models.CharField(max_length=200)

class Project(models.Model):
    project=models.CharField(max_length=200)
    startdate=models.DateField()
    enddate=models.DateField()
    description=models.TextField(max_length=2500)

class Certificate(models.Model):
    certificate=models.CharField(max_length=200)
    vendor=models.CharField(max_length=200)

class Detail(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    loca=models.CharField(max_length=200)
    summary=models.TextField(max_length=2500)
    employeeDetails=models.ManyToManyField(EmployeeDetails)
    educationDetails=models.ManyToManyField(EducationDetails)
    skillDetails=models.ManyToManyField(Skill)
    projectDetails=models.ManyToManyField(Project)
    certificateDetails=models.ManyToManyField(Certificate)
