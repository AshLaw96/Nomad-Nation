from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm
from .models import ContactMessage
from user_settings.models import Notification


def homepage(request):
    """
    Renders the homepage of the website.
    """
    return render(request, 'main/home.html')


def contact_view(request):
    """
    Handles contact form submissions and displays received messages.
    - Authenticated users can send messages to other users.
    - Unauthenticated users can only send messages to site administrators
      (superusers).
    - Displays messages received by the logged-in user.
    """
    # Default to an empty queryset if the user is not authenticated
    received_messages = ContactMessage.objects.none()

    if request.user.is_authenticated:
        # Get all messages received by the current user
        received_messages = ContactMessage.objects.filter(
            recipient=request.user
        )

    if request.method == 'POST':
        # Initialise the form with POST data and user context
        form = ContactForm(
            request.POST,
            user=request.user if request.user.is_authenticated else None
        )
        if form.is_valid():
            contact_message = form.save(commit=False)
            # Set sender as the current user, if logged in
            contact_message.sender = (
                request.user if request.user.is_authenticated
                else None
            )

            # Determine recipient:
            # - If the user is not logged in, send the message to the first
            #   available superuser
            # - Otherwise, use the recipient selected in the form
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

                # Check if notifications are enabled
                if recipient.user_profile.notifications:
                    Notification.objects.create(
                        # Recipient of the notification
                        user=recipient,
                        type=Notification.CONTACT_FORM,
                        message=(
                            _("New contact message from ") +
                            f"{sender_name}."
                        ),
                        created_by=(
                            request.user if request.user.is_authenticated
                            else None
                        ),
                    )

            # Show success message to the user
            messages.success(
                request, _("Your message has been sent successfully.")
            )
            return redirect("homepage")
    else:
        # If the request is GET, initialise an empty form
        form = ContactForm(
            user=request.user if request.user.is_authenticated else None
        )

    # Render the contact page template with the form and received messages
    return render(
        request,
        "main/contact.html",
        # Pass messages to template
        {"form": form, "received_messages": received_messages},
    )


@login_required
def delete_message(request, message_id):
    """
    View to allow a user to delete a message only if they are the recipient.
    """
    message = get_object_or_404(ContactMessage, id=message_id)

    # If the logged-in user is NOT the recipient, raise a 403 error
    if message.recipient != request.user:
        # This correctly returns a 403 instead of 404
        raise PermissionDenied

    if request.method == "POST":
        message.delete()
        messages.success(request, _("Message deleted successfully."))
        return redirect("contact")

    return redirect("contact")
