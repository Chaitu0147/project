from django.contrib import admin
from .models import Attendance,register,Student
# Register your models here.
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(register)