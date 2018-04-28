from django import forms
from .models import Careers


class CareersForm(forms.ModelForm):

    class Meta:
        model = Careers
        fields = ('name', 'email', 'contact_no', 'location',
                  'resume', 'linked_in', 'github', 'stack_overflow')


