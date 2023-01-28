from django.contrib import admin
from .models import Student,Class,Course,Subject,Teacher

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)