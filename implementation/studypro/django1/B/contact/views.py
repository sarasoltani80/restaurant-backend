from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse

def contact(request):
   if request.method == 'POST':
      #return HttpResponse('Hello')
      contact_form = ContactForm(request.POST)
      if contact_form.is_valid():
         contact_form.save()

   else:
      #return HttpResponse('Hello1')
      contact_form = ContactForm()

   context = {'contact' : contact_form}
   return render(request , 'contact.html' , context)

