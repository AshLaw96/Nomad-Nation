from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import ContactForm


User = get_user_model


def homepage(request):
    return render(request, 'main/home.html')
 
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user if request.user.is_authenticated else None)
        if form.is_valid():
            contact_message = form.save(commit=False)
            # Set sender as the current user, if logged in
            contact_message.sender = request.user if request.user.is_authenticated else None
            if not request.user.is_authenticated:
                # Send messages only to admin
                contact_message.recipient = User.objects.filter(is_superuser=True).first()
            else:
                # Authenticated users can contact specific users
                contact_message.recipient = form.cleaned_data.get('recipient')
            contact_message.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('homepage')  
    else:
        form = ContactForm(user=request.user if request.user.is_authenticated else None)

    return render(request, 'main/contact.html', {'form': form})
