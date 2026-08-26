from .email import send_email
from .webhook import send_webhook

def notify_user(user, message):
    if user.email:
        send_email(user.email, "Notification", message)
