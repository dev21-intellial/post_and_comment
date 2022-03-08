from fnmatch import fnmatchcase
from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import Post ,Comments
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
        data_store=Post(user_id=vsr,description=description)
        data_store.save()
        
        return redirect('/Added_post')
    else:
        all_posts=Post.objects.all().order_by('-id')
        return render(request,"Added_post.html",{'all_posts':all_posts})
        

       
def back(request):
    return redirect('/compose')


def post_delete(request,id):
    user_delete=Post.objects.filter(id=id)
    user_delete.delete()
    
    return redirect('/Added_post')


def pass_comment(request):
    return render(request,'pass_comment.html')

def to_save_comment(request):
    if request.method=='POST':
        user_id=request.user.id
        print(user_id)
        comment_given=request.POST['comment_txtArea']
        print(comment_given)
        
        data_store=Comments(post__User_id=user_id,desciption=comment_given)
        print(data_store)
        data_store.save()
        return HttpResponse("your data stored in database successfully")
    else:
        return HttpResponse("your comment data saved")



