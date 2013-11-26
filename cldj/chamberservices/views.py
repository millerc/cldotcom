from django.shortcuts import render_to_response
from django.template import RequestContext

from chamberservices.forms import ProposalRequestForm

def request_proposal(request):
    form = ProposalRequestForm
    return render_to_response("chamberservices/proposal_request.html", {
        "form": form,
    }, context_instance=RequestContext(request))        
