import json
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render

from .models import *

from rest_framework.views import APIView
from django.http import JsonResponse



class DegreeApi(APIView):
    def get(self, request, format=None):
        data = json.loads(request.body)
        if data['course_name'] is None or data['user_id'] is None:
            return JsonResponse({'detail' : "Bad request","error" : True, "data" : None}, status=400)
        
        course_name= data['course_name']
        user_id= data['user_id']
        
        # Get student using user_id
        student = Student.objects.get(user_id=user_id)
        course = Course.objects.filter(title= course_name).first()
        student_course_degree = StudentDegree.objects.filter(student=student, course=course).first()
        print(student_course_degree)
        if student_course_degree is not None:
            return JsonResponse({"student": student.id, "course_name": course.title, "degree": student_course_degree.degree})
        else:
            return JsonResponse({'detail' : "No result found!","error" : True, "data" : None}, status=404)

class ClassInfoApi(APIView):
    def get(self, request, format=None):
        data = json.loads(request.body)
        if data['course_name'] is None:
            return JsonResponse({'detail' : "Bad request","error" : True, "data" : None}, status=400)
        
        course_name= data['course_name']
        # 
        course = Course.objects.filter(title= course_name).first()
        class_data = Class.objects.filter(course= course)
        classes = []
        if class_data is not None:
            for class_info in class_data:
                classes.append({"course_title": course.title, 
                                 "class_title": class_info.title ,
                                 "class_day": class_info.claas_day,
                                 "start_time": class_info.start_time,
                                 "end_time": class_info.end_time,
                                 "lecturer": "{} {}".format(class_info.lecturer.user.first_name, class_info.lecturer.user.last_name)
                                 })
            return JsonResponse(classes,safe=False)

        else:
            return JsonResponse({'detail' : "No result found!","error" : True, "data" : None}, status=404)


def branches(request):
    ctx = {
        'branches': Branche.objects.all()
    }
    return render(request, 'university/branches.html', ctx)

def faculties(request):
    ctx = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'university/faculties.html', ctx)

def courses(request):
    ctx = {
        'courses': Course.objects.all()
    }
    return render(request, 'university/courses.html', ctx)
