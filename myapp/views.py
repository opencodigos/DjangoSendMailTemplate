from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactMeForm

from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import EmailMultiAlternatives 
from weasyprint import HTML     
import weasyprint


def sendmail_contact_to_pdf(data):
    body = 'Mensagem de texto' # opcional no lugar de html_body
    
    html_body = get_template('send.html').render(data) 
    
    # html para pdf
    response = HttpResponse(content_type='application/pdf')
    pdf = html_body.format(**data)
    
    response['Content-Disposition'] = 'filename=certificate_{}'.format(data['name']) + '.pdf'
    pdf = weasyprint.HTML(string=pdf, base_url='http://127.0.0.1:8000/media').write_pdf(stylesheets=[weasyprint.CSS(string='body { font-family: serif}')]) 
    
    email = EmailMultiAlternatives(data['subject'], html_body, settings.DEFAULT_FROM_EMAIL, to=['leticialimacgi@gmail.com'])
    email.attach("emailpdf_{}".format(data['name']) + '.pdf', pdf, "application/pdf")
    email.attach_alternative(html_body, "text/html")
    email.content_subtype = "pdf"  
    email.decode = 'us-ascii'
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
            sendmail_contact_to_pdf(data) # Aqui vou criar uma função para envio
            # chamei de sendmail_contact

            return redirect('contact')
    else:
        form = ContactMeForm()
    return render(request, 'form-contact.html', {'form': form})