from django.shortcuts import render
from email import message
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from RoyalCars.settings import BASE_DIR
from django.views import View
from .models import Form, Project, handle_uploaded_file


class Home(LoginRequiredMixin, View):
    template_name = 'index.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()[:5]
        self.context["projects"] = projects
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        form = Form.objects.create(full_name=name, email=email, subject=subject, message=message)
        form.save()
        return redirect('/')


class About(View):
    template_name = 'about.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Booking(View):
    template_name = 'booking.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Car(View):
    template_name = 'Car.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Contact(View):
    template_name = 'Contact.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Detail(View):
    template_name = 'detail.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Service(View):
    template_name = 'service.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Team(View):
    template_name = 'team.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Testimonial(View):
    template_name = 'testimonial.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

