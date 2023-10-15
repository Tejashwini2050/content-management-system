from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import post

# Create your views here.
def index(request):
    data = post.objects.all()
    return render(request=request,template_name='cms/index.html',context={'data':data})

def read(request,post_id):
    if post_id:
        Post=post.objects.filter(pk=post_id)


    return render(request=request,template_name='cms/read.html',context={'post':Post.get()})

def delete(request,post_id):
    if post_id:
         P=post.objects.filter(pk=post_id)
         P.delete()
         return HttpResponse("Post has been successfully deleted")

    return HttpResponse("Insert proper post_id")

def create(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']  # Assuming 'image' is the name in your form
        video = request.FILES['video']
        post.objects.create(title=title,content=content,image=image,video=video)
        return redirect('/')
    return render(request=request,template_name='cms/create.html')

def update(request,post_id):
    if post_id:
        Post=post.objects.filter(pk=post_id)
    if request.POST:
        n_t=request.POST['title']
        n_c=request.POST['content']
        
        Post.update(title=n_t,content=n_c)
        return redirect('/')
    return render(request=request,template_name='cms/update.html',context={'post':Post.get()})
