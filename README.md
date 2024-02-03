# Django Envio de E-mail Template HTML para PDF (Weasyprint)

Converter um arquivo HTML para PDF e enviar esse arquivo por e-mail via anexo. Para isso vamos utilizar uma biblioteca incrivel chamana Weasyprint. É uma biblioteca gratuita para uso basico que vai atender o que precisamos nesse vídeo. Vocês podem olhar a site oficial e verificar os exemplo. 

Vídeo Tutorial [Link](https://www.youtube.com/watch?v=jz0f6giWfbI)


Repositório Inicial: https://github.com/djangomy/sendmail-template


Vamos utilizar a bilbioteca nativa do Django para envio de e-mail. **EmailMultiAlternatives**. Tem muito mais recursos que o EmailMessage.

Na documentação tem um exemplo que vamos seguir 

[https://docs.djangoproject.com/en/4.1/topics/email/](https://docs.djangoproject.com/en/4.1/topics/email/)

Mas antes vamos precisar configurar nosso servidor para envio de email. *(não vamos utilizar backend email do django não. Fica tranquilo)* **Vamos configurar envio de e-mail real.**

Eu vou utilizar Host do outlook.com, mas pode ser qualquer um de sua preferencia. Gmail, yahoo, mail.

Para usar uma configuração diferente você precisará do HOST, PORT, TLS.
As demais informações você preenche com suas credenciais. 

*core/settings.py*

```python
# Host do outlook tenho essas configurações.

EMAIL_HOST = 'smtp.office365.com' 
EMAIL_HOST_USER = 'seu e-mail do outlook' 
EMAIL_HOST_PASSWORD = 'sua senha do outlook' 
EMAIL_PORT = 587 
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'seu email do outlook'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
```

*myapp/views.py*

Para pegar as informações do formulário e disparar o email, vamos utilizar `request.POST.get()`

```python
def contact_me(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST) 
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
             
            # data, puxo as informações dos campos name, email, subject.
            data = { 
                'name': request.POST.get('name'), 
                'email': request.POST.get('email'),
                'subject': request.POST.get('subject'),
            }
            
            sendmail_contact_to_pdf(data) # Aqui vou criar uma função para envio
						# chamei de sendmail_contact_to_pdf

            return redirect('contact')
    else:
        form = ContactMeForm()
    return render(request, 'form-contact.html', {'form': form})
```

Vamos criar uma função para envio de e-mail. Está igual a documentação, apenas acrescentei um detalhe. ***get_template*** para ler o template.html e .render(data) renderiza as informações no template. Então html_body que é nosso template será enviado no e-mail. 

Como Vamos gerar um PDF e enviar por anexo vou utilizar uma bilblioteca incrivel. Weasyprint (é free).

```python
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
    
    sendmail = EmailMultiAlternatives('Formulário de Contato', html_body, settings.DEFAULT_FROM_EMAIL, to=['leticialimacgi@gmail.com'])
    sendmail.attach("emailpdf_{}".format(data['name']) + '.pdf', pdf, "application/pdf")
    sendmail.attach_alternative(html_body, "text/html")
    sendmail.content_subtype = "pdf"  
    sendmail.decode = 'us-ascii'
    return sendmail.send()
```

Cria um template para envio de e-mail. Chamei de send.html

*myapp/templates/send.html* 

```html
{% extends 'base.html' %} 
{% block title %}Formulário de Contato{% endblock %}

{% block content %}

<h1>Envia Formulario de contato</h1>

<p>{{name}}</p>
<p>{{email}}</p>
<p>{{subject}}</p>

<img src="https://i.ibb.co/SBqzC0f/mark.jpg" alt="hero-image" width="250"/>

<p>
  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minima eligendi odio
  harum sed, pariatur quos quas veniam beatae quis hic blanditiis quasi iure
  quaerat eaque nulla corporis, voluptatem inventore earum.
</p>

<span>Copyright &#169; 2021 Leticia Lima. All&nbsp;rights&nbsp;reserved.</span>

{% endblock %}
```

`python manage.py runserver`

Django Envio de E-mail com Template HTML Customizavél no corpo do e-mail [Link](https://github.com/djangomy/sendmail-template)

