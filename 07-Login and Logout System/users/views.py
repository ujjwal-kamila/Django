from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterFrom

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created✅ You are now able to Login")
            return redirect('login')
    else:
        form = UserRegisterFrom()
        
    return render(request,'users/register.html',{'form': form})


# NewUser Test@123
# NewUser2 Test@1234

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')