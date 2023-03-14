from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from django.core.mail import send_mail
from contact.models import Contact

# Contact Form
class ContactView(TemplateView):
    template_name = "contact.html"
    def post(self,request):
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            comment = request.POST["comments"]
            print("name :",name,"email :",email,"subject:",subject,"comment:",comment)
            # messages.success(request, name)
            c = Contact()
            c.name=name,
            c.email=email,
            c.subject=subject,
            c.comment=comment,
            c.save()
            if name and email and subject and comment != "":
                subject = "Thank You"
                from_mail = 'jobcy@support.com'
                message = "Thank you for contact us"
                send_mail(subject, message, from_mail, [email],fail_silently=False)
                return redirect("/contact")