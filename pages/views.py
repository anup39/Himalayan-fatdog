from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect

from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string

from django.contrib import messages

from .models import AboutUsPage, Enquiry, Member,Booking

import smtplib


def about_us(request):
    about = AboutUsPage.objects.all().first()
    members = Member.objects.all()
    context = {
        'about':about,
        'members':members,
    }
    return render(request, 'pages/about_us.html', context)


def contact_us(request):
    message = request.POST.get('message')
    full_name = request.POST.get('full_name')
    email = request.POST.get('email')


    company = request.POST.get('company')
    country = request.POST.get('country')
    phone = request.POST.get('phone')
    
    if full_name and email and message:
        enquiry = Enquiry(
            full_name=full_name,
            email=email,
            message=message,
            company=company,
            country=country,
            phone=phone,
            )
        enquiry.save()
        msg = "Thank you for contacting us, we will get back to you as soon as possible."
        messages.success(request, msg)
    else:
        msg = "something went wrong , please try again later."
        messages.error(request, msg)

def success(request):
    return render(request, "pages/success.html", {})

def why_with_us(request):
    about = AboutUsPage.objects.all().first()
    members = Member.objects.all()
    context = {
        'about':about,
        'members':members,
    }
    return render(request, 'pages/why_with_us.html',context)

def booking_form(request):
    return render(request,'pages/booking_form.html')



def booking_success(request):
    return render(request, "pages/booking_success.html", {})


def handle_booking(request):
    message = request.POST.get('message')
    full_name = request.POST.get('full_name')
    email = request.POST.get('email')
    package = request.POST.get('package')
    country = request.POST.get('country')
    phone = request.POST.get('phone')
    
    if full_name and email and message and package:
        booking = Booking(
            full_name=full_name,
            email=email,
            message=message,
            package=package,
            country=country,
            phone=phone,
            )
        booking.save()

        # MAIL SENDER HERE

        subject, from_email, to = 'Received From Booking Form', 'Himalaya Treks Nepal', 'himalayatreksnepal@gmail.com'
        text_content = 'This is an important message.'
        html_content = render_to_string('emailBookTemplate.html', {'emailNameREP': 'Booking','nameREP': full_name, 'emailREP': email, 'countryREP': country, 'phoneREP': phone, 'messageREP': message, 'packageREP': package})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        msg = "Thank you for your booking, we will get back to you as soon as possible."
        messages.success(request, msg)
    else:
        msg = "something went wrong , please try again later."
        messages.error(request, msg)

    return redirect("pages:booking_success")


def legal(request):
    about = AboutUsPage.objects.all().first()
    members = Member.objects.all()
    context = {
        'about':about,
        'members':members,
    }
    return render(request,'pages/legal.html',context)

def corona(request):
    return render(request,'pages/corona.html')

def enquiry(request):
    return render(request,'pages/enquiry.html')


def handle_enquiry(request):
    message = request.POST.get('message')
    full_name = request.POST.get('full_name')
    email = request.POST.get('email')
    country = request.POST.get('country')
    phone = request.POST.get('phone')
    
    if full_name and email and message and phone:
        booking = Booking(
            full_name=full_name,
            email=email,
            message=message,
            country=country,
            phone=phone,
            )
        booking.save()

        # MAIL SENDER HERE

        subject, from_email, to = 'Received From Enquiry Form', 'Himalaya Treks Nepal', 'himalayatreksnepal@gmail.com'
        text_content = 'This is an important message.'
        html_content = render_to_string('emailTemplate.html', {'emailNameREP': 'Enquiry','nameREP': full_name, 'emailREP': email, 'countryREP': country, 'phoneREP': phone, 'messageREP': message})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        msg = "Thank you for contacting us, we will get back to you as soon as possible."
        messages.success(request, msg)
    else:
        msg = "something went wrong , please try again later."
        messages.error(request, msg)


    return redirect("pages:success")

def who_we_are(request):
    about = AboutUsPage.objects.all().first()
    members = Member.objects.all()
    context = {
        'about':about,
        'members':members,
    }
    return render(request, 'pages/who_we_are.html',context)
