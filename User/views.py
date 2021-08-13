from User.models import User1,Post
from User.forms import RegForm , PostForm,LoginForm

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .decoretors import unauthenticated_user



def home(request):
    context={}
    if request.user.is_authenticated:
        myposts=Post.objects.all().filter(user=request.user).order_by('-created_at')
        print(myposts)
        context['myposts'] = myposts
    return render(request,'user/home.html',context)

# Create your views here.
@unauthenticated_user
def login(request):
    if request.method=='POST':
        loginform= LoginForm(data=request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            user=auth.authenticate(request,email=email,password=password)   
            
            if user is not None:
                auth.login(request,user)
                #print(user.is_authenticated)
                #print('login',request.user)
                messages.success(request,'You are logged in')
                return redirect('home')
            else:
                messages.warning(request,'invalid crediantions')
                return redirect('login')

        else:
            messages.warning(request,'invalid crediantions')
            return redirect('login')

    return render(request,'user/login.html', {'LoginForm':LoginForm})



# we cannot create a func name as logout # becaause django has inbuilt logout fun
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')



@unauthenticated_user
def register(request):
    if request.method=='POST':
        regform= RegForm(request.POST)
        if regform.is_valid():
            first_name = regform.cleaned_data['first_name']
            last_name = regform.cleaned_data['last_name']
            email = regform.cleaned_data['email']
            username = regform.cleaned_data['username']
            password = regform.cleaned_data['password']
            repeat_password = request.POST['repeat_password']

            if password == repeat_password:
                if  User1.objects.filter(username=username).exists():
                    messages.warning(request,'username exists')
                    return redirect('register')
                else:
                    if User1.objects.filter(email=email).exists() :
                        messages.warning(request,'email already exists')
                        return redirect('register')
                    else:
                        user=User1.objects.create_user(username=username,email=email,password=password)
                        user.first_name=first_name
                        user.last_name=last_name
                        user.save()

                        messages.success(request,"Account created successfuly")
                        return redirect('login')
            else:
                messages.warning(request,'Password does not match')
                return redirect('register')
        else:
            messages.warning(request,'Invalid Info')
            return redirect('register')

   
    return render(request,'user/signup.html',{'RegForm': RegForm})

@login_required
def post(request):
    context = {}
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user=request.user
            post1=Post(text=text,user=user)
            post1.save()
            return redirect('home')
    if request.method=="GET":
        form = PostForm()
        context['PostForm'] = PostForm
        return render(request,'user/postform.html',context)



