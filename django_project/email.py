from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


class EmailService:

    @staticmethod
    def send_verification_email(user, verification_link):

        subject = "Verify Your Email"

        context = {
            "user": user,
            "verification_link": verification_link
        }

        html_content = render_to_string(
            "emails/verification_email.html",
            context
        )

        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )

        email.attach_alternative(html_content, "text/html")
        email.send()