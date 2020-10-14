from django import forms


class ContactForm(forms.Form):
    """ A contact form class """

    
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=124, required=True)
    message = forms.CharField(max_length=1024, widget=forms.Textarea, required=True)
