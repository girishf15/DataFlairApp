from dataflair.settings import EMAIL_HOST_USER
from django.shortcuts import render

from .forms import Subscribe
from django.core.mail import send_mail

# Create your views here.

#Send Email
def subscribe(request):

    sub = Subscribe()

    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Jumanji'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})

    return render(request, 'index.html', {'form':sub})
