from django.shortcuts import render

from .models import *


from rest_framework.parsers import JSONPasrser
from django.http.response import JSONResponse




# class DegreeApi(APIView):
#     def getdegreeApi(request, format=None):
#         if request.method=='GET':
#             degree = StudentDegree.objects.all()
#             get_degree = StudentDegree (degree, many =True)
#             return JSONResponse(get_degree.data)
        

class class DegreeApi(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        if data['course_name'] is None or data['user_id'] is None:
            return JsonResponse({'detail' : "Bad request","error" : True, "data" : None}, status=400)
        
        query_degree = (course_name= data['course_name'], user_id= data['user_id'])
        if query_degree is not None:
            return JsonResponse({"course_name": Course.title})
        else:
            return JsonResponse({'detail' : "Not found","error" : True, "data" : None}, status=401)


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
