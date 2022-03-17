from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'core/index.html')



@csrf_exempt
def webhook(request):
	print(request.POST)
	return JsonResponse({"status": "OK"})
