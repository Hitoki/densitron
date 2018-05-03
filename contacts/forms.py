from django.forms import ModelForm

from contacts.models import ContactRequest


class ContactRequestCreate(ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['first_name', 'surname', 'email', 'country', 'phone',
                  'job_title', 'comments']
