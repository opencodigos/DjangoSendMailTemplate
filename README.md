# Django Envio de E-mail com Template HTML Customizavél no corpo do e-mail

Como fazer envio de e-mail com template HTML customizavél no corpo do e-mail. Para isso vamos utilizar uma biblioteca nativa do Django EmailMessage. 

Vídeo Tutorial [Link](https://youtu.be/hUBwpxoETWE)

**Configurações Iniciais**

<details><summary><b>Ambiente Virtual Linux/Windows</b></summary>

- **Ambiente Virtual Linux/Windows**
    
    
    Lembrando… Precisa ter Python instalado no seu ambiente.
    
    **Criar o ambiente virtual Linux/Windows**
    
    ```python
    ## Windows
    python -m venv .venv
    source .venv/Scripts/activate # Ativar ambiente
    
    ## Linux 
    ## Caso não tenha virtualenv. "pip install virtualenv"
    virtualenv .venv
    source .venv/bin/activate # Ativar ambiente
    ```
    
    Instalar os seguintes pacotes.
    
    ```python
    pip install django
    pip install pillow
    ```
    
    Para criar o arquivo *requirements.txt*
    
    ```python
    pip freeze > requirements.txt
    ```

</details>

<details><summary><b>Criando o Projeto</b></summary>

- **Criando o Projeto**
    
    ## **Criando o projeto**
    
    “core” é nome do seu projeto e quando colocamos um “.” depois do nome do projeto significa que é para criar os arquivos na raiz da pasta. Assim não cria subpasta do projeto.
    
    ```python
    django-admin startproject core .
    ```
    
    **Testar a aplicação**
    
    ```python
    python manage.py runserver
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b413a084-7ed1-4480-a648-5049cebeba61/Untitled.png)

</details>

<details><summary><b>Configurar Settings e Arquivos Static</b></summary>

- **Configurar Settings e Arquivos Static**
    
    ## **Vamos configurar nossos arquivos** *static*
    
    ```python
    import os 
    
    # base_dir config
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
    STATIC_DIR=os.path.join(BASE_DIR,'static')
    
    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
        }
    }
    
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    STATIC_URL = '/static/' 
    
    MEDIA_ROOT=os.path.join(BASE_DIR,'media')
    MEDIA_URL = '/media/'
    
    # Internationalization
    # Se quiser deixar em PT BR
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'
    USE_I18N = True
    USE_L10N = True 
    USE_TZ = True
    ```
    
    *urls.py*
    
    ```python
    from django.contrib import admin
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
    ```

</details>

<details><summary><b>Criando Aplicativo</b></summary>

- **Criando Aplicativo**
    
    **Vamos criar nosso aplicativo no Django.**
    
    Para criar a aplicação no Django rode comando abaixo. “myapp” é nome do seu App.
    
    ```python
    python manage.py startapp myapp
    ```
    
    Agora precisamos registrar nossa aplicação no *INSTALLED_APPS* localizado em *settings.py*.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c60b799e-edec-4c58-b8b3-35ca714f1ea5/Untitled.png)

</details>

<details><summary><b>Template base e Bootstrap Configuração</b></summary>

- **Template base e Bootstrap Configuração**
    
    ### Bootstrap configuração
    
    Doc: [https://getbootstrap.com/docs/5.2/getting-started/introduction/](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    
    Com Base na documentação para utilizar os recursos Boostrap basta adicionar as tags de CSS e JS. No HTML da Pagina Base.
    
    ```python
    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    
    <!-- JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    ```
    
    ## Template Base
    
    1 - criar um arquivo base ***base.html*** onde vamos renderizar nosso conteúdo. 
    
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>{% block title %}{% endblock %}</title>
    
    	<!-- CSS -->
    	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    
    </head>
    <body>  
    	
    	{% block content %}
    	
    	{% endblock %} 
     
    	<!-- JS-->
    	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    </body>
    </html>
    ```
    

</details>

<details><summary><b>Iniciar Aplicativo</b></summary>

- **Iniciar Aplicativo**
    
    *myapp/templates/form-contact.html*
    
    ```html
    {% extends 'base.html' %}
    {% block title %}Formulário de Contato{% endblock %}
    {% block content %}
     <h1> Formulário aqui</h1>
    {% endblock %}
    ```
    
    *myapp/views.py*
    
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def contact_me(request):
        return render(request, 'form-contact.html')
    ```
    
    criar arquivo myapp/*urls.py*
    
    ```
    from django.urls import path 
    from myapp import views
    
    urlpatterns = [
        path('', views.contact_me, name='contact'), 
    ]
    ```
    
    urls.py do projeto. ***core/urls.py***
    
    ```python
    from django.contrib import admin
    from django.urls import path, include # adicionar include
    from django.conf import settings
    from django.conf.urls.static import static 
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapp.urls')), # url do app
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
    ```
    
    Rodar o projeto para ver como está.
    
    ```python
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver
    ```

</details>

<details><summary><b>Cria modelo formulário</b></summary>

- **Cria modelo formulário**
    
    *myapp/models.py*
    
    ```python
    from django.db import models
    
    # Create your models here.
    class ContactMe(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100) 
        subject = models.CharField(max_length=100)
        message = models.TextField()
    ```
    
    Criar arquivo *myapp/forms.py*
    
    ```python
    from django import forms
    from .models import ContactMe
    
    class ContactMeForm(forms.ModelForm):
        class Meta:
            model = ContactMe
            fields = ['name', 'email', 'subject', 'message'] 
            
        def __init__(self, *args, **kwargs): # Adiciona 
            super().__init__(*args, **kwargs)  
            for field_name, field in self.fields.items():   
                  field.widget.attrs['class'] = 'form-control'
    ```
    
    *myapp/templates/*form-contact*.html*
    
    ```html
    {% extends 'base.html' %}
    {% block title %}Formulário de Contato{% endblock %}
    {% block content %}
    <form method="POST" autocomplete="off">
        <h4>Entre em contato conosco</h4>
        {% csrf_token %}
        {{form}}
        <button type="submit" class="btn btn-success">Salvar</button>
    </form>
    {% endblock %}
    ```
    
    *myapp/views.py*
    
    ```python
    from django.shortcuts import render, redirect
    from .forms import ContactMeForm
    
    # Create your views here.
    def contact_me(request):
        if request.method == 'POST':
            form = ContactMeForm(request.POST) 
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                return redirect('contact')
        else:
            form = ContactMeForm()
    
        return render(request, 'form-contact.html', {'form': form})
    ```
    
    Vamos rodar o projeto e testar.
    
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/313cc247-fd85-471e-b210-d2002cc2442f/Untitled.png)
    
    Já está salvando as informações.

</details>

<details><summary><b>Configura Envio de E-mail</b></summary>

- **Configura Envio de E-mail**
    
    
    Vamos utilizar a bilbioteca nativa do Django para envio de e-mail. **EmailMessage**.
    
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
                
                sendmail_contact(data) # Aqui vou criar uma função para envio
    						# chamei de sendmail_contact
    
                return redirect('contact')
        else:
            form = ContactMeForm()
        return render(request, 'form-contact.html', {'form': form})
    ```
    
    Vamos criar uma função para envio de e-mail. Está igual a documentação, apenas acrescentei um detalhe. ***get_template*** para ler o template.html e .render(data) renderiza as informações no template. Então message_body que é nosso template será enviado no 
    
    ```python
    from django.conf import settings 
    from django.template.loader import get_template  
    from django.core.mail import EmailMessage 
    
    def sendmail_contact(data):
        message_body = get_template('send.html').render(data)  
        sendmail = EmailMessage('Formulário de Contato', 
                                message_body, settings.DEFAULT_FROM_EMAIL,
                                to=['leticialimacgi@gmail.com'])
        sendmail.content_subtype = "html"    
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
    {% endblock %}
    ```
    
    `python manage.py runserver` 
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f300b16f-a391-4a68-8709-977dcf605487/Untitled.png)

</details>

Como Converter template HTML para PDF e enviar por e-mail com Weasyprint. [Link](https://www.youtube.com/watch?v=hUBwpxoETWE)
