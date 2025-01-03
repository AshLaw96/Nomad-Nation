from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('account_login')
    else:
        form = CustomUserRegistrationForm()
        print("empty form loaded")

    return render(request, 'account/signup.html', {'form': form})
