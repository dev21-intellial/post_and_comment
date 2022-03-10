from ast import Return
from fnmatch import fnmatchcase
from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User


from .models import Post ,Comments, Like , Dislike
from django.contrib import auth

# Create your views here.

def authenticate_user(request):
    if request.method=='POST':
        username=request.POST['fname']
        pass1=request.POST['pass1']
        user=auth.authenticate(request,username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/post')
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

def post(request):    
    if request.method=="POST":
        user_id=request.user.id
        description=request.POST['txtArea']
        data_store=Post(user_id=user_id,description=description)
        data_store.save()
        return redirect('/post')
    else:
        all_posts=Post.objects.values('id','user__username','last_update','description','user_id').order_by('-id')
        print(all_posts)
        comments=Comments.objects.values('id','post_id','comment','user__username')
        return render(request,"post/post.html",{'all_posts':all_posts,'comments':comments})
   
def post_delete(request,id):
    user_delete=Post.objects.filter(id=id)
    user_delete.delete()
    return redirect('/post')

def pass_comment(request,id):
    if request.method=='POST':
        return redirect('/pass_comment')
    else:
        return render(request,'post/pass_comment.html',{'post_id':id})

def given_comment(request,id):
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        print(post_id)
        comment_given=request.POST['comment_txtArea']
        print(comment_given)
       
        data_store=Comments(post_id=post_id,comment=comment_given,user_id=request.user.id)
        data_store.save()
        return redirect('/post')
    else:
        return render(request,'post/post.html')

def likes(request,id):
    if request.method=='POST':
        user_id=request.user.id
        print(user_id)

        data_store=Like(user_id=user_id,post_id=id)
        data_store.save()
        return redirect('/post')
    else:
        likes=Like.objects.values('user__id')
        return redirect(request,'post/post.html',{'likes':likes})

def dislike(request,id):
    if request.method=='POST':
        user_id=request.user.id
        print(user_id)
        data_store=Dislike(user_id=user_id,post_id=id)
        data_store.save()
        return redirect('/post')
    else:
        return redirect(request,'post/post.html')

    
def add_post(request):
    return redirect('/show')