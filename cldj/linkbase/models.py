from django.db import models
from datetime import timedelta

# Create your models here.

class AuthTicket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    hours = models.PositiveIntegerField()
    ticket = models.CharField(max_length=80)
    #username = models.CharField(max_length=80)
    
    def expires(self):
        return created + timedelta(hours=hours)
    
    def __unicode__(self):
        return self.ticket
        
class QuickbaseTable(models.Model):
     pass