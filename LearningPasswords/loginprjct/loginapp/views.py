from django.shortcuts import render
from loginapp.form import UserProfileInfoForm,UserForm

# Create your views here.
def index(request):
    return render(request,'loginapps/index.html')
def register(request):
    userportform= UserProfileInfoForm()
    userform=UserForm()
    registered=False
    if request.method=='POST':
        userportform = UserProfileInfoForm(data=request.POST)
        userform=UserForm(data=request.POST)
        if userportform.is_valid() and userform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            profile=userportform.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                userportform.picture= request.FILES['profile_pic']
            profile.save()
            return index(request)
        else:
            print(userform.errors,userportform.errors)
    else:
        userportform=UserProfileInfoForm()
        userform=UserForm()
    return render(request,'loginapps/registration.html',{'userportform':userportform,'userform':userform,'registered':registered})

def login(request):
    return render(request,'loginapps/login.html')
