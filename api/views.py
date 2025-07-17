from django.shortcuts import render
from django.views.generic.base import TemplateView,View
from django.views.generic import CreateView,FormView
from .forms import UserRegisteration,UserLogin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.shortcuts import redirect
# Create your views here.

class Home_view(TemplateView):
    template_name='api/home.html'
    

class Register_view(CreateView):
    template_name='api/registeration.html'
    form_class=UserRegisteration
    success_url=reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        # print("KWARGS:", kwargs)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        context['button_text'] = 'Register'
        return context

class UserLogin_view(FormView):
    
    template_name='api/registeration.html'
    form_class=UserLogin
    success_url=reverse_lazy('home')
    
    def form_valid(self,form):
        # print("request==>",self.request.user)
        # print("form==>",form)
        # print("prev_user==>",user)
        user= form.get_user()
        # print("next_user==>",user)
        login(self.request,user)
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Login'
        context['button_text'] = 'Login'
        return context
    

class UserLogout(View):
    
    def post(self,request):
        logout(request)
        return redirect('login')
    