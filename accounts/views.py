
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('part_list')  # 로그인 후 리다이렉트할 페이지
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})