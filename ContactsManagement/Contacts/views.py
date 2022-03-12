from django.shortcuts import render
from django.shortcuts import redirect
from Contacts.models import *
from Contacts.forms import *

# Create your views here.

def Contacts(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user)
        if request.method == 'GET':
            contact_form = ContactsForm()
            return render(request, 'Contacts/contacts.html', {'contact_form': contact_form, 'contacts': contacts})
        elif request.method == 'POST':
            contact_form = ContactsForm(request.POST)
            if contact_form.is_valid():
                contact_obj = contact_form.save(commit=False)
                contact_obj.user = request.user
                contact_obj.save()
                return redirect('.')
            return render(request, 'Contacts/contacts.html', {'contact_form': contact_form, 'contacts': contacts, 'failure': True})        
    return redirect('/')