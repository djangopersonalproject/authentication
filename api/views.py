from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import UserRegisteration
from django.contrib import messages
# Create your views here.

class Home_view(TemplateView):
    template_name='api/home.html'
    

class Register_view(CreateView):
    template_name='api/registeration.html'
    form_class=UserRegisteration
    success_url='/login/'
    
    def form_valid(self, form):
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # print("KWARGS:", kwargs)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        context['button_text'] = 'Register'
        return context