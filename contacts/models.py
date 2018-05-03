from django.db import models


class ContactRequest(models.Model):
    head = models.TextField()
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    country = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    job_title = models.CharField(max_length=64)
    comments = models.TextField()

    user = models.ForeignKey('company.ContactUser', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    to_email = models.CharField(max_length=255)

    def __str__(self):
        return '#{}'.format(self.id)


class DownloadDocumentUserRequest(models.Model):
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    doc_title = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return '#{}'.format(self.id)
