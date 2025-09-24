from django.contrib import admin
from .models import Courses, Instructor, SuccessStories

# Register your models here.

admin.site.register(Courses)
admin.site.register(Instructor)
admin.site.register(SuccessStories)
