from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View
import json
from django.http import JsonResponse
from django.http import HttpResponseRedirect


class LoginView(View):
    def get(self,request):
        return render(request , 'auth/login.html',{})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            # this if do so ==> if last page was artists/create and auth is needed so after log in go to artists/create automatically
            if self.request.GET.get('next'):
                return redirect(self.request.GET.get('next'))  
            else:
                return redirect('/admin')
        else:
            status = {'error': 'Invalid username or password !'}
            return render(request,'auth/login.html',status)
    
class LogoutView(View):
    def get(self,request):
        return render(request , 'auth/logout.html',{})
    
    def post(self, request):
        logout(request)
        return redirect('/logout')
    
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html',{})
    
    def post(self,request,*args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_pass = request.POST.get('re')

        if password == repeat_pass:
            try:
                if User.objects.get(username=username):
                    status = {'error': "username already exists"}
                    return render(request, 'auth/register.html',status)
            except:
                try:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    # login(request,user)
                    return redirect('/login')
                except:
                    status = {'error': "failed"}
                    return render(request, 'auth/register.html',status)
        
        status = {'error': "password doesn't match"}
        return render(request, 'auth/register.html',status)
