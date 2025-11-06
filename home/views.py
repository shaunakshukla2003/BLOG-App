from django.shortcuts import render,HttpResponse ,get_object_or_404,redirect
from .models import Contact, Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    allPosts = Post.objects.all()
    context ={'allPosts':allPosts}
    return render(request,'home.html',context)

@login_required(login_url='')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        issue=request.POST['issue']
        
        if len(name)<2 or len(email)<3 or len(number)<10 or len(issue)<4:
            messages.error(request,"Please fil the correct deatils")
        else:
            contact=Contact(name=name,email=email,number=number,issue=issue)
            contact.save()
            messages.success(request,'Successfully saved')  
    return render(request,'contact.html')


def about(request):
    pass
                                              ### CRUD OPERATION ###
# Read(details)
def blog(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog.html',context)


## CREATing BLOG

@login_required(login_url='')
def newblog(request):
    if request.method =='POST':
        title = request.POST['title']
        content = request.POST['content']
        featured_image = request.FILES.get("featured_image")
        new = Post(title=title,content=content,image=featured_image,author=request.user) #request.user is the user instance means request.user will check the user is logged in or not
        new.save()
        messages.success(request,"POSTED")
        return redirect('/')
        
    return render(request,'newblog.html')

##Editing the blog
def editblog(request,slug):
    post=get_object_or_404(Post,slug=slug, author=request.user) #get_object_or_404 is the function in django is conveninet shorcut to retrieve a single object from DB
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        new_image=request.FILES.get("featured_image")
        if new_image:
            post.image = new_image
        post.save()
        messages.success(request,"Edited Successfully")
        
        return redirect('/')
    return render(request,'editblog.html',{'post':post})

##DELETing BLOG
def deleteblog(request,slug):
    post = get_object_or_404(Post,slug=slug,author=request.user)
    if request.method == 'POST':
       post.delete()
       messages.error(request,"DELETED SUCCESSFULY")
       return redirect('/')
    return render(request,'deleteblog.html',{'post':post})    