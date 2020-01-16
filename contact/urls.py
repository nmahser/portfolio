from django.contrib import admin
from django.urls import path
import contact.views
from django.utils.encoding import uri_to_iri


urlpatterns = [
    path('', contact.views.contactForm, name='contact'),
    path('success/', contact.views.successView, name='success'),
]
