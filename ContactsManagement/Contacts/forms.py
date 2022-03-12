from django import forms
from Contacts.models import *

class ContactsForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(ContactsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label.title()
            self.fields[field].widget.attrs['autocomplete'] = "new-password"
    
    class Meta:
        model = Contact
        fields = ('email', 'name', 'phone_number')