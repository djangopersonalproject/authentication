from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models  import User
from django import forms
from .models import Note
class UserRegisteration(UserCreationForm):
    password1 =  forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='password confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,label="email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
    
class UserLogin(AuthenticationForm):
    username = forms.CharField(required=True,label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True,label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields =['title','content']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'row':10,'col':50,'class':'form-control'}),
        }
        
    


