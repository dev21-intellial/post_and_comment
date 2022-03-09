from fnmatch import fnmatchcase
from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User


from .models import Post ,Comments, Like
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
    return render(request,'post/login.html')


def registration(request):
    return render(request,'post/registration.html')


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
        users=User.objects.values('id','username','email')
        return render(request,'post/show.html',{'users':users})
    

def compose(request):
    return render(request,'post/compose.html')

def Added_post(request):    
    if request.method=="POST":
        vsr=request.user.id
        description=request.POST['txtArea']
        data_store=Post(user_id=vsr,description=description)
        data_store.save()
        return redirect('/Added_post')
    else:
        all_posts=Post.objects.values('id','user','last_update','description').order_by('-id')
       
        return render(request,"post/Added_post.html",{'all_posts':all_posts})
           
def back(request):
    return redirect('/compose')

def post_delete(request,id):
    user_delete=Post.objects.filter(id=id)
    user_delete.delete()
    return redirect('/Added_post')


def pass_comment(request,id):
    if request.method=='POST':
        return redirect('/pass_comment')
    else:
        return render(request,'post/pass_comment.html',{'post_id':id})


def given_comment(request):
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        print(post_id)
        comment_given=request.POST['comment_txtArea']
        print(comment_given)
       
        data_store=Comments(post_id=post_id,comment=comment_given)
        data_store.save()
        return redirect('/comments')
    else:
        return render(request,'Added.html')

def comments(request):
    comments=Comments.objects.values('comment')
    return render(request,'post/comments.html',{'comments':comments})

