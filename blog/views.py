from django.shortcuts import redirect, render
from .models import Blog

# Create your views here.
def allblogs(request):
    modelResponse = Blog.objects.all()
    print(modelResponse)
    return render(request,'blog/allblogs.html',{"allblogs" : modelResponse})

def readblog(request,id):
    modelResponse = Blog.objects.get(id=id)
    return render(request, 'blog/readblog.html', {"blog": modelResponse})

def addblog(request):
    return render(request, 'blog/addblog.html')

def savenewblog(request):
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        thumbnail = request.POST["thumbnail"]
        
        newobject = Blog(title=title, body=body , thumbnail=thumbnail)
        newobject.author = request.user
        newobject.save()

        return redirect('/blog/allblogs/')
