from django.contrib import admin

from contactus.models import ContactListing, Message

# Register your models here.

admin.site.register(ContactListing)
admin.site.register(Message)
