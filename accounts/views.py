from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        'profile': user.userprofile,
    }
    return render(request, 'accounts/profile.html', context)
