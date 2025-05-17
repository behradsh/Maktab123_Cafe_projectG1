from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['user_email', 'title', 'description']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description: 
            raise forms.ValidationError('This field cannot be null.')
        if len(description) > 1000:
            raise forms.ValidationError('Descriptions cannot exceed 1000 characters.')
        return description