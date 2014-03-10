from django.shortcuts import render_to_response, RequestContext

# Create your views here.

def home(request):
    variable = None
    return render_to_response("cafe/home.html", {
        "variable": variable,
    }, context_instance=RequestContext(request))        
