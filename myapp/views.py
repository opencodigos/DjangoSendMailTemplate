from django.shortcuts import render, redirect
from .forms import ContactMeForm

from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import EmailMessage 

def sendmail_contact(data):
    message_body = get_template('send.html').render(data)  
    email = EmailMessage(data['subject'],
                            message_body, settings.DEFAULT_FROM_EMAIL,
                            to=['leticialimacgi@gmail.com'])
    email.content_subtype = "html"    
    return email.send()

# Create your views here.
def contact_me(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST) 
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
             
            # data, puxo as informações dos campos name, email, subject, message.
            data = { 
                'name': request.POST.get('name'), 
                'email': request.POST.get('email'),
                'subject': request.POST.get('subject'),
                'message': request.POST.get('message'),
            } 
            sendmail_contact(data) # Aqui vou criar uma função para envio
            # chamei de sendmail_contact

            return redirect('contact')
    else:
        form = ContactMeForm()
    return render(request, 'form-contact.html', {'form': form})