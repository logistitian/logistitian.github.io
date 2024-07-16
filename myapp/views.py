from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})

def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    return render(request, 'delete_user.html', {'user': user})
