from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile, Follow


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('profile')

    return render(request, 'users/registration.html')


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        profile = get_object_or_404(Profile, user=user)
        profile.bio = request.POST.get('bio', profile.bio)
        profile.profile_picture = request.FILES.get('profile_picture', profile.profile_picture)
        profile.save()

        return redirect('profile')
    else:
        profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/edit_profile.html', {'profile': profile})



@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if request.user != user_to_follow:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile')



@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(follower=request.user, following=user_to_unfollow).first()
    if follow:
        follow.delete()
    return redirect('profile')

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
