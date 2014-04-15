from django import forms

class VoucherForm(forms.Form):
    project_code = forms.CharField(max_length=16)
    subject = forms.CharField(max_length=64,initial="New CommunityLink Chamber Publication Now Available")
    sender_name = forms.CharField(max_length=64,initial="CommunityLink")
    sender_title = forms.CharField(max_length=64,initial="Accounts Specialist")
    sender_email = forms.EmailField(initial="service@communitylink.com")