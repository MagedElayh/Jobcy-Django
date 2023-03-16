from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutUs(models.Model):
    image = models.ImageField(
        _("image background"), 
        upload_to="static/image/aboutus",
        help_text="width and height for image must be 640px * 360px"
    )
    header = models.CharField(_("header"), max_length=200)
    paragraph = models.TextField(_("paragraph"))

    def __str__(self):
        return self.header


class SectionTwo(models.Model):
    image = models.ImageField(
        _("image background"), 
        upload_to="static/image/aboutus",
        help_text="width and height for image must be 1920px * 1227px"
    )
    text = models.TextField(_("text"))