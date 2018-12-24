from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'username': username,
                'password': password,
                'has_error': True
            }
            return render(request, 'login.html', context=context)
        else:
            login(request, user=user)
            return redirect('project_list')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('project_list')