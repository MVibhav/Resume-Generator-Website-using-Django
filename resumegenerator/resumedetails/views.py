from django.shortcuts import render,redirect
from .models import Detail,EmployeeDetails,EducationDetails,Skill,Project,Certificate
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def details(request):
    if(request.method == 'POST'):
        firstname=request.POST.get("firstname","")
        lastname=request.POST.get("lastname","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        loca=request.POST.get("loca","")
        summary=request.POST.get("summary","")
        empdetailslis=[]
        edudetailslis=[]
        skilllis=[]
        projectlis=[]
        vendlis=[]
        for i in range(0,10):
            try:
                jobtitle=request.POST.get("jobtitle"+str(i+1),"")
                employer=request.POST.get("employer"+str(i+1),"")
                empstartdate=request.POST.get("empstartdate"+str(i+1),"")
                empenddate=request.POST.get("empenddate"+str(i+1),"")
                empcity=request.POST.get("empcity"+str(i+1),"")
                empdescription=request.POST.get("empdescription"+str(i+1),"")
                emp1=EmployeeDetails(jobtitle=jobtitle,employer=employer,startdate=empstartdate,enddate=empenddate,city=empcity,description=empdescription)
                emp1.save()
                empdetailslis.append(emp1)
            except:
                break
        
        for i in range(0,10):
            try:
                school=request.POST.get("school"+str(i+1),"")
                degree=request.POST.get("degree"+str(i+1),"")
                edustartdate=request.POST.get("edustartdate"+str(i+1),"")
                eduenddate=request.POST.get("eduenddate"+str(i+1),"")
                educity=request.POST.get("educity"+str(i+1),"")
                edudescription=request.POST.get("edudescription"+str(i+1),"")
                percent=request.POST.get("edupercent"+str(i+1),"")
                edu1=EducationDetails(school=school,degree=degree,startdate=edustartdate,enddate=eduenddate,city=educity,percent=percent,description=edudescription)
                edu1.save()
                edudetailslis.append(edu1)
            except:
                break
        
        for i in range(0,30):
            try:
                skill=request.POST.get("skill"+str(i+1))
                skill1=Skill(skill=skill)
                skill1.save()
                skilllis.append(skill1)
            except:
                break
        
        for i in range(0,30):
            try:
                project=request.POST.get("projectname"+str(i+1),"")
                projstartdate=request.POST.get("projstartdate"+str(i+1),"")
                projenddate=request.POST.get("projenddate"+str(i+1),"")
                projdescription=request.POST.get("projdescription"+str(i+1),"")
                proj1=Project(project=project,startdate=projstartdate,enddate=projenddate,description=projdescription)
                proj1.save()
                projectlis.append(proj1)
            except:
                break
        
        for i in range(0,30):
            try:
                certificate=request.POST.get("certificatename"+str(i+1))
                vendor=request.POST.get("vendorname"+str(i+1))
                vend1=Certificate(certificate=certificate,vendor=vendor)
                vend1.save()
                vendlis.append(vend1)
            except:
                break

        detail=Detail(firstname=firstname,lastname=lastname,email=email,phone=phone,loca=loca,summary=summary)
        detail.save()
        detail.employeeDetails.set(empdetailslis)
        detail.save()
        detail.educationDetails.set(edudetailslis)
        detail.save()
        detail.skillDetails.set(skilllis)
        detail.save()
        detail.projectDetails.set(projectlis)
        detail.save()
        detail.certificateDetails.set(vendlis)
        detail.save()
    return render(request,'resumedetails/details.html')

def resume(request,id):
    reqresume=Detail.objects.get(id=id)
    template=loader.get_template("resumedetails/resume.html")
    html=template.render({"reqresume":reqresume})
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
        "print-media-type": None
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type="application/pdf")
    response["Content-Disposition"]="attachment; filename=resume.pdf"
    return response

def allusers(request):
    objs=Detail.objects.all()
    return render(request,"resumedetails/allusers.html",{'objs':objs})

def deluser(request,id):
    obj=Detail.objects.get(id=id)
    if(request.method=='POST'):
        obj.delete()
        return redirect('allusers')
    return render(request,'resumedetails/deluser.html',{'obj':obj})

def employeedetails(request):
    if(request.method == 'POST'):
        jobtitle=request.POST.get("jobtitle","")
        employer=request.POST.get("employer","")
        startdate=request.POST.get("startdate","")
        enddate=request.POST.get("enddate","")
        city=request.POST.get("city","")
        description=request.POST.get("description","")

        employeedetail=EmployeeDetails(jobtitle=jobtitle,employer=employer,startdate=startdate,enddate=enddate,city=city,description=description)
        employeedetail.save()
        return redirect('details')
    return render(request,'resumedetails/employeedetails.html')

def viewresume(request,id):
    reqresume=Detail.objects.get(id=id)
    return render(request,'resumedetails/resume.html',{'reqresume':reqresume})