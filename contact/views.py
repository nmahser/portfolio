
from contact.models import Contact
from django import forms
from .forms import ContactForm
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from contact.tasks import sendEmailTask
from jobs.models import Job
from contact.models import Contact
from django.contrib import messages


def contactForm(request):

    jobs = Job.objects  # Save jobs

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # get user's inputs
            form.save()
            subject = form.cleaned_data.get('subject')
            from_email = form.cleaned_data.get('from_email')
            message = form.cleaned_data.get('message')

            try:
                # send email
                sendEmailTask.delay(subject, message, from_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found. Please send an email to mahsernihat@gmail.com')
            return redirect('success')
        else:
            pass
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form, 'jobs': jobs})


'''
def contactForm(request):
    jobs = Job.objects  # Save jobs

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            redirect('success')

        else:
            print(form.errors)
            redirect('failed')

    else:
        form = ContactForm()

    context = {'form': form, 'jobs': jobs}

    return render(request, 'contact.html', context)

'''
'''
def contactForm(request):
    jobs = Job.objects  # Save jobs
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success')

    return render(request, "contact.html", {'form': form, 'jobs': jobs})



def contactForm(request):
    jobs = Job.objects  # Save jobs
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('valid')
            redirect('contact')
        else:
            print(form.errors)

    else:
        form = ContactForm()

    context = {'form': form, 'jobs': jobs}

    return render(request, "contact.html", context)
'''

'''
def contactForm(request):
    jobs = Job.objects  # Save jobs
    if request.method == 'GET':
        form = ContactForm()
        form = ContactForm(request.POST or None)
        if form.is_valid():
            print("!")
            subject = form.cleaned_data.get('subject')
            from_email = form.cleaned_data.get('from_email')
            message = form.cleaned_data.get('message')
            # form = ContactForm()
            # try:
            #    sendEmailTask.delay(subject, message, from_email)
            # except BadHeaderError:
            #    return HttpResponse('Invalid header found.')
            # return redirect('success')
        formDict = {'form': form, 'jobs': jobs}
    return render(request, "contact.html", context=formDict)

'''


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


'''
def contactForm(request):
    if request.method == 'GET':
        form = ContactForm()
        jobs = Job.objects  # Save jobs

    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data.get('subject')

            from_email = form.cleaned_data.get('from_email')

            message = form.cleaned_data.get('message')

            try:
                sendEmailTask.delay(subject, message, from_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

        else:

            subject = form.cleaned_data.get('subject')

            from_email = form.cleaned_data.get('from_email')

            message = form.cleaned_data.get('message')

            if from_email is None:
                raise forms.ValidationError('Not a valid email')

    return render(request, "contact.html", {'form': form, 'jobs': jobs})
'''
'''
 try:
                subject = form.cleaned_data['subject']
            except:
                raise forms.ValidationError('Not a valid subject')

            if from_email is None:
                raise forms.ValidationError('Not a valid email')
            try:
                message = form.cleaned_data['message']
            except:
                raise forms.ValidationError('Not a valid message')
'''

'''
form = ContactForm(request.POST)
        if form.is_valid():
            try:
                subject = form.cleaned_data['subject']
            except:
                raise forms.ValidationError('Not a valid subject')

            try:
                from_email = form.cleaned_data['from_email']
            except:
                raise forms.ValidationError('Not a valid email')

            try:
                message = form.cleaned_data['message']
            except:
                raise forms.ValidationError('Not a valid message')

            try:
                sendEmailTask.delay(subject, message, from_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
'''
