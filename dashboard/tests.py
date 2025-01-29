from django.http import JsonResponse
from django.contrib.auth.models import User, ContactMessage


def test_create_message(request):
    try:
        # Fetch sender and recipient with more detailed error handling
        sender = User.objects.get(id=5)
    except User.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "error": "Sender user not found."
        })
    except User.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "error": "Sender user not found."
        })
    try:
        recipient = User.objects.get(id=5)
    except User.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "error": "Recipient user not found."
        })
    # Create the ContactMessage
    message = ContactMessage.objects.create(
        sender=sender,
        recipient=recipient,
        subject="Test Subject",
        message="This is a test message."
    )
    return JsonResponse({"status": "success", "message_id": message.id})