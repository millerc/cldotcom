from django import forms
from django.forms import ModelForm
from chamberservices.models import ProposalRequest

class ProposalRequestForm(ModelForm):
    class Meta:
        model = ProposalRequest
        exclude = ('',)
        widgets = {
            'products': forms.CheckboxSelectMultiple(attrs={'class':'label'}),
            'delivery_method': forms.RadioSelect(attrs={'class':'label'}),
        }