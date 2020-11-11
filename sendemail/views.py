from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
def contactView(request):
    """ inspired by learndjango.com tutorial """
    
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject, 
                    message, 
                    from_email, 
                    ['krisztian.keseru@gmail.com']
                )
                messages.success(request, 'Your message was sent! Thank you \
                                 for your message.')
            except BadHeaderError:
                messages.error(request, 'Error! Your message was not sent. \
                               Please try it again later or call us.')
            return redirect('success')
    return render(request, 'sendemail/email.html', {'form': form})

def successView(request):
    return redirect('contact')