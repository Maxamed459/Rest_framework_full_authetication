import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings

def create_otp():
    otp=""
    for i in range(6):
        otp +=str(random.randint(1, 9))
    return otp

def send_email_user(email):
    user = User.objects.get(email=email)
    otp_code = create_otp()
    OneTimePassword.objects.create(user=user, code=otp_code)

    subject = "One-Time Passcode for Email Verification"
    current_site = "bixi-dhiig.vercel.app"  # or dynamically use request if needed

    email_body = (
        f"Hi {user.first_name},\n\n"
        f"Thanks for signing up on {current_site}.\n"
        f"Please verify your email using this one-time passcode:\n\n"
        f"👉 {otp_code}\n\n"
        f"This code will expire soon.\n\n"
        f"Best regards,\nBixi Dhiig Team"
    )

    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )

    email.send(fail_silently=False)  # better for debugging
    print("Email sent successfully")