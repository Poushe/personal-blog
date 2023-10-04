from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .models import blog, author
from .form import blogForm
from .authorform import authorForm

def userblogform(request):
    userblog=blogForm()
    if request.method=='POST':
        userblog=blogForm(request.POST)
        if userblog.is_valid():
            userblog.save()
            return redirect('http://127.0.0.1:8000/')
    context={'userblog':userblog}
    return render(request, 'blog/blog-form.html', context)

def allblog(request):
    seeallblog=blog.objects.all()
    context={'seeallblog':seeallblog}
    return render(request, 'blog/index.html',context)

def userblogformupdate(request,pk):
    singleblog=blog.objects.get(id=pk)
    blogcontent=blogForm(instance=singleblog)
    if request.method=='POST':
        blogcontent=blogForm(request.POST, instance=singleblog)
        if blogcontent.is_valid():
            blogcontent.save()
            return redirect('http://127.0.0.1:8000/')
    context={"blogcontent":blogcontent}
    return render(request,'blog/update-form.html',context)

def addauthorform(request):
    authorF=authorForm()
    if request.method=='POST':
        authorF=authorForm(request.POST)
        if authorF.is_valid():
            authorF.save()
    context={'authorF':authorF}
    return render(request, 'blog/add-author.html', context)

def deleteblog(request,pk):
    delblog=blog.objects.get(id=pk)
    if request.method=='POST':
        delblog.delete()
        return redirect('http://127.0.0.1:8000/')
    context={'delblog':delblog}
    return render(request,'blog/delete-blog.html',context)