from django.shortcuts import render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.http import Http404

from chamberservices.forms import ProposalRequestForm

def request_proposal(request):
    form = ProposalRequestForm()
    if request.method == 'POST':
        form = ProposalRequestForm(request.POST)
        if form.is_valid():
            form.save()

    return render_to_response('chamberservices/proposal_request.html', {
        'form': form,
    }, context_instance=RequestContext(request))        

def default(request, slug):
    page_name = slug
    try:
      return render_to_response('chamberservices/%s.html' % slug, {
          'page_name': page_name,
      }, context_instance=RequestContext(request))
    except TemplateDoesNotExist: 
      raise Http404        
