from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

# Create your views here.

def home(request):
    variable = None
    return render_to_response("frontpage/home.html", {
        "variable": variable,
    }, context_instance=RequestContext(request))        
