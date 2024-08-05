from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Video, Comment
from .forms import VideoSearchForm, CommentForm, UserRegisterForm

def video_list(request):
    form = VideoSearchForm(request.GET)
    videos = Video.objects.all()
    if form.is_valid():
        query = form.cleaned_data['query']
        videos = videos.filter(title__icontains=query)
    return render(request, 'video_list.html', {'form': form, 'videos': videos})

@login_required
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    is_liked = video.likes.filter(id=request.user.id).exists()
    comments = video.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.video = video
            new_comment.user = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('video_detail', args=[video.id]))
    else:
        comment_form = CommentForm()

    return render(request, 'video_detail.html', {
        'video': video,
        'is_liked': is_liked,
        'total_likes': video.total_likes(),
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })

@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if video.likes.filter(id=request.user.id).exists():
        video.likes.remove(request.user)
    else:
        video.likes.add(request.user)
    return HttpResponseRedirect(reverse('video_detail', args=[video.id]))

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('video_list')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('video_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
