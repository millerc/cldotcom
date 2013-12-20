from django.shortcuts import render_to_response
from django.template import RequestContext

from chamberservices.forms import ProposalRequestForm

def request_proposal(request):
    form = ProposalRequestForm()
    if request.method == 'POST':
        form = ProposalRequestForm(request.POST)
        if form.is_valid():
            form.save()

    return render_to_response("chamberservices/proposal_request.html", {
        "form": form,
    }, context_instance=RequestContext(request))        

def default(request):
    variable = None
    return render_to_response("chamberservices/default.html", {
        "variable": variable,
    }, context_instance=RequestContext(request))        
