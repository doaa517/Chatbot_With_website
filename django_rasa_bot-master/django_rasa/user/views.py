import json
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user.models import Student
from university.models import StudentDegree

from rest_framework.views import APIView
from django.contrib.auth import authenticate

class LoginApi(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        if data['username'] is None or data['password'] is None:
            return JsonResponse({'detail' : "Bad request","error" : True, "data" : None}, status=400)
        
        user = authenticate(username= data['username'], password= data['password'])
        if user is not None:
            return JsonResponse({"user_id": user.id})
        else:
            return JsonResponse({'detail' : "Unauthorized","error" : True, "data" : None}, status=401)

class UserLogin(LoginView):
    template_name='user/login.html'
    next_page="/user/profile"
    
    
    
class UserLogout(LogoutView):
    template_name='user/logout.html'
    next_page="/"
    
    
@login_required(login_url='/user/login/')
def profile(request):
    template_name = "user/profile.html"
    student = Student.objects.get(user=request.user)
    
    ctx = {
        'degrees': StudentDegree.objects.filter(student=student)
    }
    
    return render(request, 'user/profile.html', ctx)

# class LoginView(InvalidFormMixin, BaseLoginView):
#     """
#     Login view
#     """
#     # http_method_names = ['post']
#     form_class = AuthenticationForm
#     template_name = 'account/login.html'
#     allow_authenticated = False

#     def get_form_kwargs(self):
#         kw = super(LoginView, self).get_form_kwargs()
#         kw.update({'request': self.request})
#         return kw

#     def form_valid(self, form):

#         login(self.request, form.get_user())
#         message = _("Welcome back, %s! Redirecting ...") % form.get_user().name
#         url = self.get_success_url()
#         if self.request.GET.get('amount') and self.request.GET.get('gateway'):
#             amount = self.request.GET.get('amount')
#             gateway = self.request.GET.get('gateway')
#             project = self.request.GET.get('project')
#             url = url + '?amount=' + amount + '&gateway=' + gateway + '&project=' + project
#         data = {
#             'message': message,
#             'redirect_url': url
#         }

#         if not form.cleaned_data.get('remember_me'):
#             self.request.session.set_expiry(0)

#         return JsonResponse(data, status=200)
