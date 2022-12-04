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