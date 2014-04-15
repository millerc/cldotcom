from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from linkbase import quickbase
from linkbase.forms import VoucherForm

# Create your views here.

def email_vouchers(voucher_form_data):
    voucher_data = quickbase.get_voucher_data(voucher_form_data['project_code'])
    t = get_template('linkbase/sponsor-delivery-notice.txt')
    for i, sponsor in enumerate(voucher_data['sponsors']):
        d = Context({ 'project':voucher_data['project'], 'sponsor':sponsor, 'sender':voucher_form_data })
        voucher_data['sponsors'][i]['sent'] = send_mail(
            voucher_form_data['subject'], 
            t.render(d), 
            '%s <%s>' % (voucher_form_data['sender_name'], voucher_form_data['sender_email']), 
            [ '%s <%s>' % (sponsor['billing_contact'], sponsor['billing_contact_email']) ], 
            fail_silently=False
            )
    voucher_data['sample_message'] = t.render(d).replace('\n', '<br />')
    return voucher_data
            
@login_required            
def vouchers(request):
    voucher_data = {'project':'','sponsors':'','sample_message':''}
    form = VoucherForm(initial={
            'sender_name': '%s %s' % (request.user.first_name, request.user.last_name),
            'sender_title': 'Accounts Specialist',
            'sender_email': request.user.email,
            'subject': 'New CommunityLink Chamber Publication Now Available' })
    if request.method == 'POST':
        form = VoucherForm(request.POST)
        if form.is_valid():
            voucher_data = email_vouchers(form.cleaned_data)

    return render_to_response("linkbase/vouchers.html", {
        "form": form,
        "project": voucher_data['project'],
        "sponsors": voucher_data['sponsors'],
        "sample_message": voucher_data['sample_message'],
    }, context_instance=RequestContext(request))        
