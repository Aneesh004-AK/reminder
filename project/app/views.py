from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,LoginForm
from .forms import ReminderForm
from .models import Reminder



def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request,"signup.html",{'form':form})
    
    
    
    
def login(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
        
            

@ login_required                   
def home(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('home')
    else:
        form = ReminderForm()

    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'home.html', {'form': form, 'reminders': reminders})
   
   
def delete(request,id):
    reminder = Reminder.objects.get(id=id)
    if reminder.user == request.user:
        reminder.delete()
    return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('login')


