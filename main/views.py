from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm
from .models import ContactMessage
from user_settings.models import Notification


def homepage(request):
    return render(request, 'main/home.html')


def contact_view(request):
    # Default to an empty queryset if the user is not authenticated
    received_messages = ContactMessage.objects.none()

    if request.user.is_authenticated:
        # Get all messages received by the current user
        received_messages = ContactMessage.objects.filter(
            recipient=request.user
        )

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

            # Determine recipient
            if not request.user.is_authenticated:
                recipient = User.objects.filter(is_superuser=True).first()
            else:
                recipient = form.cleaned_data.get('recipient')

            # Ensure there's a recipient before saving
            if recipient:
                contact_message.recipient = recipient
                contact_message.save()

                # Notify recipient of the new contact message
                sender_name = (
                    contact_message.sender.username
                    if contact_message.sender
                    else _("Guest")
                )

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
            return redirect("homepage")
    else:
        form = ContactForm(
            user=request.user if request.user.is_authenticated else None
        )

    return render(
        request,
        "main/contact.html",
        # Pass messages to template
        {"form": form, "received_messages": received_messages},
    )


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(
        ContactMessage, id=message_id, recipient=request.user
    )

    if request.method == "POST":
        message.delete()
        messages.success(request, _("Message deleted successfully."))

    # Redirect back to the contact page
    return redirect("contact")
