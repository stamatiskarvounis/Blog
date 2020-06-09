from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

widgets ={
'name':forms.TextInput(attrs={'class':'input','placeholder':'Your name'})
}
