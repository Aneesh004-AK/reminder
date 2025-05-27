from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Reminder
from django import forms




class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']




class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
        
        
        
        
        
        
        # remider   form
class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['message', 'Timer', 'mode']
        widgets = {
            'message': forms.TextInput(attrs={'placeholder': 'Enter your reminder message', 'class': 'form-control'}),
            'Timer': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'mode': forms.Select(attrs={'class': 'form-select'}),
        }

