from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from articles.models import Article





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)


        if form.is_valid():
                # send email code goes here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(email,form.cleaned_data['message'])




            send_mail(
            'Message from ' + name,#subject
            message,#message
            email,# from email
            ['stamkarblog@gmail.com'],#To email

            )

            # send_mail (
            # subject,
            # message,
            # from_email,
            # recipient_list,
            # fail_silently: bool=False,
            # auth_user: NoneType=None,
            # auth_password: NoneType=None,
            # connection: NoneType=None,
            # html_message: NoneType=None
            # )




            #send_mail('New Enquiry', message, sender_email, ['stamkarblog@gmail.com'])



            return render(request,"articles/thankyou.html")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
