from django.contrib import admin
from .models import Detail,EmployeeDetails,EducationDetails,Skill,Project,Certificate
# Register your models here.
admin.site.register(Detail)
admin.site.register(EmployeeDetails)
admin.site.register(EducationDetails)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certificate)