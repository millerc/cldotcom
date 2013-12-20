from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField

class ProposalProduct(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class ProposalRequest(models.Model):

    QUANTITY_CHOICES = (
        (1000, '1,000'),
        (2500, '2,500'),
        (5000, '5,000'),
        (7500, '7,500'),
        (10000, '10,000'),
        (10001, 'More than 10,000'),
    )
    
    DELIVERY_MONTHS_CHOICES = (
        (3, 'Within 3 months'),
        (6, 'Within 6 months'),
        (9, 'Within 9 months'),
        (12, 'Within 12 months'),
    )
    
    DECISION_TIME_CHOICES = (
        (2, 'Within 1 or 2 weeks'),
        (4, 'Within 1 month'),
        (13, 'Within 3 months'),
        (26, 'Within 6 months'),
        (52, 'Within 12 months'),
        (0, 'Just looking'),
    )
    
    LAST_PROJECT_CHOICES = (
        (1, 'Within the past year'),
        (2, 'Between 1 and 2 years ago'),
        (3, 'Between 2 and 3 years ago'),
        (99, 'Do not know'),
        (0, 'This would be the first time'),
    )
    
    DELIVERY_METHOD_CHOICES = (
        ('UPS', 'UPS'),
        ('INPERSON', 'Schedule a personal visit'),
        ('WEB', 'Schedule a web-based presentation'),
        ('EMAIL', 'Email'),
    )
    
    organization = models.CharField(max_length=128)
    contact = models.CharField(max_length=64, verbose_name='Point of contact')
    phone = PhoneNumberField()
    email = models.EmailField()
    website = models.URLField()
    address = models.CharField(max_length=128, verbose_name='Mailing address')
    city = models.CharField(max_length=64)
    state = USStateField()
    zip = models.CharField(max_length=10)
    
    products = models.ManyToManyField(ProposalProduct, 
        verbose_name='Choose all of the products you are interested in.')
    quantity = models.PositiveIntegerField(choices=QUANTITY_CHOICES, 
        verbose_name='How many do you need?')
    delivery_months = models.PositiveIntegerField(choices=DELIVERY_MONTHS_CHOICES, 
        verbose_name='When do you need them?')
    decision_time = models.PositiveIntegerField(choices=DECISION_TIME_CHOICES, 
        verbose_name='When do you anticipate making your decision?')
    last_project = models.PositiveIntegerField(choices=LAST_PROJECT_CHOICES, 
        verbose_name='When was the last time you did such a project?')
    delivery_method = models.CharField(max_length=16,choices=DELIVERY_METHOD_CHOICES, 
        verbose_name='How would you like us to deliver your custom proposal?',
        default=None,
        )
    
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.organization, self.created)
