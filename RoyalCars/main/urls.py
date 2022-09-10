from django.urls import path
from .views import Home, About, Booking, Car, Contact, Detail, Service, Team, Testimonial

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('booking', Booking.as_view(), name='booking'),
    path('car', Car.as_view(), name='car'),
    path('contact', Contact.as_view(), name='contact'),
    path('detail', Detail.as_view(), name='detail'),
    path('service', Service.as_view(), name='service'),
    path('team', Team.as_view(), name='team'),
    path('testimonial', Testimonial.as_view(), name='testimonial'),
]
