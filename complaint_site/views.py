from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method=="POST":
        form=ApplicationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            bp=form.cleaned_data["bp"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            complaint = form.cleaned_data["complaint"]
            explain=form.cleaned_data["explain"]
            print(first_name)

            Form.objects.create(first_name=first_name,last_name=last_name,bp =bp,email=email,date=date,complaint=complaint,explain=explain)

            message_body=f"Your complain was registered.Thank You \n {first_name} (BP No.-{bp}) "


            email_message=EmailMessage("Complain Registered",message_body,to=[email])
            email_message.send()
            messages.success(request, "Form submitted successfully")


    return render(request, "index.html")


def about(request):
    return render(request, "about.html")



