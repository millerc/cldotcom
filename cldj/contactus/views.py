from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from contactus.models import ContactListing
from contactus.forms import MessageForm

# Create your views here.

def contact_list(request):
    message_saved = None
    form = MessageForm()
    contacts = ContactListing.objects.filter(active=True)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            message_saved = True

    return render_to_response("contactus/contact_list.html", {
        "contacts": contacts,
        "form": form,
        "message_saved": message_saved
    }, context_instance=RequestContext(request))        
