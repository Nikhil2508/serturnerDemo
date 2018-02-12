from django.views import View
from django.shortcuts import render



class BaseView(View):

    def get(self,request,*args, **kwargs):
        return render(request,"index.html",{})

class LoginView(View):

    def get(self,request,*args, **kwargs):
        return render(request,"login.html",{})
