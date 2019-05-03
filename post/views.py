from django.shortcuts import render, redirect
from .models import Post, Hashtag, HASHTAG_CHOICES
from .forms import PostForm, HashtagForm, EditPostForm, UserForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    temp = 'hashtag/main.html'
    return render(request,'post/trial.html',{})
'''
def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('view', pk=new_post.pk)
        else:
            form = AuthenticationForm()
        return render(request, 'post/login_user.html', {'form':form})
'''

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,request.FILES, instance=User())
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user = request.user
            user.set_password(user.password)
            user.save()
            registered = True
            if registered == True:
                return redirect('/login', pk=user.pk)
            else:
                return redirect("Username already in use.")
    else:
        user_form = UserForm()
    return render(request,'post/register.html',{'user_form':user_form})

def my_post(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(user=logged_in_user)
    return render(request, 'post/my_post.html', {'posts': logged_in_user_posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

def hashtag_list(request):
    hashtags = HASHTAG_CHOICES
    return render(request, 'hashtag/hashtag_list.html', {'hashtags': hashtags})

def hashtag_art(request):
    posts = Post.objects.filter(hname__contains="art")
    return render(request, 'hashtag/art.html', {'posts': posts})

def hashtag_fashion(request):
    posts = Post.objects.filter(hname__contains="fashion")
    return render(request, 'hashtag/fashion.html', {'posts': posts})

def hashtag_food(request):
    posts = Post.objects.filter(hname__contains="food")
    return render(request, 'hashtag/food.html', {'posts': posts})

def hashtag_mood(request):
    posts = Post.objects.filter(hname__contains="mood")
    return render(request, 'hashtag/mood.html', {'posts': posts})

def hashtag_tech(request):
    posts = Post.objects.filter(hname__contains="tech")
    return render(request, 'hashtag/tech.html', {'posts': posts})

def hashtag_wildlife(request):
    posts = Post.objects.filter(hname__contains="wildlife")
    return render(request, 'hashtag/wildlife.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        #hform = HashtagForm(request.POST, instance=Hashtag())
        pform = PostForm(request.POST,request.FILES, instance=Post())
        if pform.is_valid():


            new_post = pform.save(commit=False)
            #new_post.user = request.user
            new_post.date = timezone.now()
            new_post.save()
            return redirect('post_detail', pk=new_post.pk)
        return render(request, 'post/post_list.html', {})
    else:
        #hform = HashtagForm(instance = Hashtag())
        pform = PostForm(instance=Post())
    return render(request, 'post/create_post.html', {'post_form': pform})

'''def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})
'''
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

'''def post_edit(request, pk):
    if request.method == "POST":
        #hform = HashtagForm(request.POST, instance=Hashtag())
        uform = EditPostForm(request.POST,request.FILES, instance=Post())
        if uform.is_valid():
            uform.save()
            return redirect('post_detail', pk=new_post.pk)
    else:
        #hform = HashtagForm(instance = Hashtag())
        uform = EditPostForm(request.POST,request.FILES, instance=Post())
    return render(request, 'post/post_edit.html', {'postu_form': uform})'''
'''def post_edit(request, pk):
    posts = Post.objects.get(id=pk)
    #posts = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None,
                        request.FILES or None, instance=Post())
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=form.pk)
    return render(request, 'post/post_edit.html', {'posts': posts}) '''

def post_delete(request, pk, title):
    uform = Post.objects.get(title=title).delete()
    return render(request, 'post/post_delete.html', {'postu_form': uform})

class PostDelete(DeleteView):
    template_name = 'post/post_delete.html'
    model = Post
    success_url = '/view'

'''class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_edit.html'
    success_url = 'post/post_detail.html' '''


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None,
                        request.FILES or None, instance=Post())
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           return redirect('post_detail',pk=form.pk)
    return render(request, 'post/post_edit.html', {'form': form})
