from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about-us', views.about_us , name='about_us' ),
    path('contact-us', views.contact_us , name='contact_us' ),
    path('enquiry-success', views.success , name='success' ),
    path('why_with_us',views.why_with_us, name='why_with_us'),
    path('booking_form',views.booking_form,name='booking_form'),
    path('Booking',views.handle_booking,name='handle_booking'),
    path('Enquiry',views.handle_enquiry,name='handle_enquiry'),
    path('corona',views.corona,name='corona'),
    path('legal',views.legal,name='legal'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('who_we_are',views.who_we_are, name='who_we_are'),
    # path('Enquiry',views.display_enquiry,name='display_enquiry'),
    path('booking_success', views.booking_success , name='booking_success' ),

]
