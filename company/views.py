from django.views.generic import TemplateView

class About(TemplateView):
    template_name = "company/about.html"
class Services(TemplateView):
    template_name = "company/services.html"
class Team(TemplateView):
    template_name = "company/team.html"
class Pricing(TemplateView):
    template_name = "company/pricing.html"
class PrivacyPolicy(TemplateView):
    template_name = "company/privacy-policy.html"
class FAQs(TemplateView):
    template_name = "company/faqs.html"