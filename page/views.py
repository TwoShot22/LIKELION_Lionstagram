from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts' : posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "detail.html", {'post':post})

def new(request):
    if request.method == "POST":
        post= Post()
        post.author = request.user
        post.content = request.POST['content']
        # image 파일이 있으면 post 객체에 저장
        if 'image' in request.FILES:
            post.image= request.FILES['image']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/detail/'+str(post.id))
    return render(request, "new.html")