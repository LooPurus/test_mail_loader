from django.shortcuts import render, redirect
from .models import EmailMessage

from .forms import EmailAccountForm


def add_email_account(request):
    if request.method == 'POST':
        form = EmailAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_list')
    else:
        form = EmailAccountForm()

    return render(request=request, template_name='mail_app/add_email_account.html', context={'form': form})
