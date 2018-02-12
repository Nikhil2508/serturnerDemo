from django.views import View
from django.shortcuts import render



class BaseView(View):

    def get(self,request,*args, **kwargs):
        return render(request,"index.html",{})

class LoginView(View):

    def get(self,request,*args, **kwargs):
        return render(request,"page_user_login_1.html",{})
