from django.db import models

# Create your models here.

class ContactListing(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    title = models.CharField(max_length=64)
    extension = models.CharField(max_length=5)
    
    active = models.BooleanField()
    
    def __unicode__(self):
        return self.name
        
class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.created)