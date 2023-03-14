from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    date = models.DateTimeField(_("send date"), auto_now_add=True)
    name = models.CharField(_("Name"), max_length=200)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phone"), max_length=254, blank=True, null=True)
    message = models.TextField(_("Message"))

    def __str__(self):
        return self.name + " | " + str(self.date.date())
    

class FollowUs(models.Model):
    show_facebook = models.BooleanField(_("show Facebook"))
    facebook_link = models.URLField(_("facebook line"), max_length=200,null=True,blank=True)
    show_twitter = models.BooleanField(_("show twitter"))
    twitter_link = models.URLField(_("twitter line"), max_length=200,null=True,blank=True)
    show_dribbble = models.BooleanField(_("show dribbble"))
    dribbble_link = models.URLField(_("dribbble line"), max_length=200,null=True,blank=True)
    show_behance = models.BooleanField(_("show behance"))
    behance_link = models.URLField(_("behance line"), max_length=200,null=True,blank=True)
    show_pinterest = models.BooleanField(_("show pinterest"))
    pinterest_link = models.URLField(_("pinterest line"), max_length=200,null=True,blank=True)
    show_google_plus = models.BooleanField(_("show google-plus"))
    google_plus_link = models.URLField(_("google-plus line"), max_length=200,null=True,blank=True)
    show_lindedin = models.BooleanField(_("show linkedin"))
    lindedin_link = models.URLField(_("linkedin line"), max_length=200,null=True,blank=True)



class Location(models.Model):
    company_name = models.CharField(_("company name"), max_length=100)
    latitude = models.FloatField(_("latitude of company location"),help_text="go to google map and get latitude of your company loacation ex. 25.90009")
    longitude = models.FloatField(_("longitude of company location"),help_text="go to google map and get longitude of your company loacation ex. 25.90009")

    def __str__(self):
        return self.company_name
    