from django.contrib import admin

from .models import *

class FacultyAdmin(admin.ModelAdmin):
    list_filter = ("branche", "open_date")
    list_display = ("name", "branche")

class StudntDegreeAdmin(admin.ModelAdmin):
    list_filter = ("course", "student", "degree")
    
class PreCourseAdmin(admin.ModelAdmin):
    list_filter = ("course", "prev_course")
   
admin.site.register(University)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Branche)
admin.site.register(Course)
admin.site.register(PreCourse,PreCourseAdmin)
admin.site.register(Class)
admin.site.register(StudentDegree, StudntDegreeAdmin)


