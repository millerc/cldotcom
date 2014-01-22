from django.contrib import admin

from chamberservices.models import ProposalProduct, ProposalRequest

admin.site.register(ProposalRequest)
admin.site.register(ProposalProduct)