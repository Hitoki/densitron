from __future__ import absolute_import

from django.core.mail import EmailMessage

from densitron.celery import app

from company.models import Admin


@app.task()
def send_email_to_admins(subject, message, from_email, attached_files=None):
    mail = EmailMessage(
        subject, message, from_email,
        [admin.email for admin in Admin.objects.filter(get_emails=True)])
    if attached_files:
        for attached_file in attached_files:
            mail.attach_file(attached_file)
    return mail.send()