from django import forms


class ContactForm(forms.Form):
    """ A contact form class """

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=124, required=True)
    message = forms.CharField(max_length=1024, widget=forms.Textarea,
                              required=True)

    class Meta:
        fields = ('from_email', 'subject', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'from_email': 'Enter your email address',
            'subject': 'Subject',
            'message': 'Enter your message',
        }

        self.fields['from_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
