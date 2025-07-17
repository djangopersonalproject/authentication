from django.shortcuts import render
from django.views.generic.base import TemplateView,View
from django.views.generic import CreateView,FormView
from .forms import UserRegisteration,UserLogin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .models import Note
from .forms import NoteForm
# Create your views here.

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
    
class NoteCreateView(CreateView):
    model=Note
    form_class = NoteForm
    template_name = 'api/create.html'
    success_url = reverse_lazy('note_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "create"
        context['button_text'] = 'Submit'
        return context
    
    
class Notelist_view(ListView):
    model= Note
    template_name='api/home.html'
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    

class NoteDetail_view(DetailView):
    model=Note
    template_name='api/detail.html'
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteUpdate_view(UpdateView):
    model = Note
    form_class = NoteForm
    template_nam='api/update.html'
    success_url=reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Data'
        context['button_text'] = 'Update'
        return context

class NoteDelete_view(DeleteView):
    model=Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('home')