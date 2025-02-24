from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm


def homepage(request):
    return render(request, 'main/home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(
            request.POST,
            user=request.user if request.user.is_authenticated else None
        )
        if form.is_valid():
            contact_message = form.save(commit=False)
            # Set sender as the current user, if logged in
            contact_message.sender = (
                request.user if request.user.is_authenticated else None
            )
            if not request.user.is_authenticated:
                # Send messages only to admin
                contact_message.recipient = User.objects.filter(
                    is_superuser=True
                ).first()
            else:
                    else _("Guest")

                Notification.objects.create(
                    user=recipient,
                    type=Notification.CONTACT_FORM,
                    message=(
                        _("New contact message from ") + f"{sender_name}."
                    ),
                    created_by=(
                        request.user if request.user.is_authenticated else None
                    ),
                )

            messages.success(
                request, _("Your message has been sent successfully.")
            )
            return redirect('homepage')
    else:
        form = ContactForm(
            user=request.user if request.user.is_authenticated else None
        )

        messages.success(request, _("Message deleted successfully."))
