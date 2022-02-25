from fnmatch import fnmatchcase
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import Post
from django.contrib import auth
# Create your views here.

def authenticate_user(request):
    if request.method=='POST':
        username=request.POST['fname']
        pass1=request.POST['pass1']
        user=auth.authenticate(request,username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/show')
        else:
            return HttpResponse("your password is incorrect")  
    else:
        return HttpResponse("your password is incorrect")


def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')


def add_user(request):
    if request.method=='POST':
        username=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        myuser=User.objects.create_user(username,email,pass1)

        myuser.save()
        return redirect('/')
    else:
        return HttpResponse("404-not found page")

    

def show(request):
        users=User.objects.all()
        return render(request,'show.html',{'users':users})
    


def compose(request):
    return render(request,'compose.html')



def Added_post(request):    
    if request.method=="POST":
        vsr=request.user.id
        description=request.POST['txtArea']
        data_store=Post(user_id=vsr,desciption=description)
        data_store.save()
        all_posts=Post.objects.all().order_by('-id')
        return render(request,'added_post.html',{'all_posts':all_posts})
    else:
       return HttpResponse("Try Again:")
       

def back(request):
    return redirect('/compose')


def delete(request,id):
    user_delete=Post.objects.get(id=id)
    print(user_delete)
    user_delete.delete()
    return redirect('/Added_post')

