from django import forms
from helloworld.models import Message
from django.utils.safestring import mark_safe

class ContactForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField(required=False)
    text = forms.CharField(
                            widget=forms.Textarea(attrs={'vertical-align':'bottom'}), 
                            label=mark_safe("Message") 
                            )
    class Meta:
        model = Message
        exclude = ['time', 'display']
    

    



