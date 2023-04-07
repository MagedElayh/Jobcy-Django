from xml.dom import ValidationErr
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Header(models.Model):
    # title field using charfield constraint with unique constraint
    menu = models.CharField(max_length=200, unique=False)
    menu1 = models.CharField(max_length=200, unique=False)
    menu2 = models.CharField(max_length=200, unique=False)
    menu3 = models.CharField(max_length=200, unique=False)
    menu4 = models.CharField(max_length=200, unique=False)
    menu5 = models.CharField(max_length=200, unique=False)
    menu6 = models.CharField(max_length=200, unique=False)

    created_on = models.DateTimeField()
 
    # meta for the class
    class Meta:
        ordering = ['-created_on']
    # used while managing models from terminal
    def __str__(self):
        return self.menu
    
    class Meta:
        verbose_name_plural = "01. Header (Menu)"



class Slider(models.Model):
    # title field using charfield constraint with unique constraint
    image_slide   = models.ImageField(verbose_name=_("image_slide"), upload_to="media/image/slider")
    text_header_slide = models.CharField(max_length=200, unique=False)
    text2_slide = models.CharField(max_length=200, unique=False)
    text3_slide = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.text_header_slide
    
    class Meta:
        verbose_name_plural = "02. Sliders"





class SectionUnderSlider(models.Model):
    section_name = models.CharField(max_length=200, unique=False)
    header_section = models.CharField(max_length=200, unique=False)
    paragraph_section = models.TextField(max_length=2000)

    def __str__(self):
        return self.section_name
    
    class Meta:
        verbose_name_plural = "03. Section Under Slider (Best Sulotions)"

class SectionUnderSliderIcon(models.Model):
    # title field using charfield constraint with unique constraint
    icon = models.CharField(max_length=200, unique=False)
    header = models.CharField(max_length=200, unique=False)
    paragraph = models.CharField(max_length=2000, unique=False)
    section =models.ForeignKey(SectionUnderSlider, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.header





class SectionTwo(models.Model):    
    image   = models.ImageField(verbose_name=_("image_slide"), upload_to="media/image/home")
    header = models.CharField(max_length=200, unique=False)
    paragraph = models.CharField(max_length=1000, unique=False)

    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name_plural = "04. Section (We are Creative)"
    

class Progress(models.Model):    
    item   = models.CharField(max_length=2000, unique=False)
    precent = models.IntegerField(
        verbose_name=_("precent"),
        default=0,validators=[MaxValueValidator(100), MinValueValidator(0)]
        )
    section = models.ForeignKey(SectionTwo,models.CASCADE, null=True)

    def __str__(self):
        return self.item

class NumbersSection(models.Model):
    number = models.CharField(max_length=200, unique=False)
    text = models.CharField(max_length=200, unique=False)
    
    class Meta:
        verbose_name_plural = "05. Section Numbers"

    def __str__(self):
        return self.text


class Numbers(models.Model):
    number1 = models.CharField(max_length=200, unique=False)
    text1 = models.CharField(max_length=200, unique=False)




class SectionThree(models.Model):
    section_name = models.CharField(max_length=200, unique=False)
    header = models.CharField(max_length=200, unique=False)
    paragraph = models.CharField(max_length=1000, unique=False)

    def __str__(self):
        return self.section_name
    
    class Meta:
        verbose_name_plural = "06. Section Our Best solutions"
    

class SectionThreeIcon(models.Model):
    icon = models.CharField(
        max_length=200, unique=False,
        help_text="Go to the https://fontawesome.com/search website and search for the name of the icon and put it in this field for example fa-user"
        )
    header = models.CharField(max_length=200, unique=False)
    paragraph = models.CharField(max_length=2000, unique=False)
    section_three = models.ForeignKey(SectionThree, on_delete=models.CASCADE,null=True)





class PorfolioItem(models.Model):
    name = models.CharField(_("name"), max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "071. Our Latest Portfolio Item"


class porfolioDetail(models.Model):
    image   = models.ImageField(verbose_name=_("image"), upload_to="media/image")
    text_description = models.TextField(max_length=2000)
    porfolioItem = models.ForeignKey(PorfolioItem, on_delete=models.CASCADE,blank=True)
    
    class Meta:
        verbose_name_plural = "07. Our Latest Portfolio"


class Portfolio(models.Model):
    name_section = models.CharField(verbose_name=_("name"),max_length=200)
    # image = models.ForeignKey(porfolioDetail, on_delete=models.CASCADE)
    paragraph = models.TextField(max_length=2000, unique=False)

    def __str__(self):
        return self.name_section

    def save(self, *args, **kwargs):
        if not self.pk and Portfolio.objects.exists():
            return
        return super(Portfolio, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "07. Our Latest Portfolio"



class SectionFourProfessional(models.Model):
    image_background = models.ImageField(verbose_name=_("image"), upload_to="media/image")
    name_section = models.CharField(verbose_name=_("name section"),max_length=200)
    header = models.CharField(max_length=200, unique=False)
    paragraph = models.CharField(max_length=2000, unique=False)

    def __str__(self):
        return self.name_section
    

    class Meta:
        verbose_name_plural = "08. We Are Professional"




class SectionFiveOurTeams(models.Model):
    header = models.CharField(max_length=200, unique=False)
    paragraph = models.TextField(max_length=2000, unique=False)
    
    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "09. Our Team Members"

#Section Five our Teams
class SectionImage(models.Model):
    image   = models.ImageField(verbose_name=_("image of team"), upload_to="media/image")
    text_description = models.CharField(max_length=2000)
    user_name = models.CharField(_("name of team"), max_length=50)
    department = models.CharField(_("department"), max_length=50)
    team = models.ForeignKey(SectionFiveOurTeams, on_delete=models.CASCADE,blank=True)
    
    


class SectionSixCustomersSay(models.Model):
    image_background = models.ImageField(verbose_name=_("image background section"), upload_to="media/image")
    header = models.CharField(max_length=200, unique=False)

    def __str__(self) -> str:
        return self.header
    
    class Meta:
        verbose_name_plural = "10. What Our Customers Say"

class CustomersSay(models.Model):
    customer_icon = models.ImageField(verbose_name=_("customer icon"), upload_to="media/image")
    paragraph = models.CharField(max_length=2000, unique=False)
    customer_name = models.CharField(max_length=2000, unique=False)
    customer_name2 = models.CharField(max_length=2000, unique=False)
    customer_say = models.ForeignKey(SectionSixCustomersSay, on_delete=models.CASCADE,blank=True)




 
class NewsSection(models.Model):
    header = models.CharField(max_length=200, unique=False)

    def __str__(self) -> str:
        return self.header
    
    class Meta:
        verbose_name_plural = "11. Our Latest News"


class NewsImage(models.Model):
    image   = models.ImageField(verbose_name=_("news image"), upload_to="media/image/news")
    date = models.DateField(auto_now=False,auto_now_add=False)
    Header_paragraph = models.CharField(max_length=200, unique=False)
    text_description = models.TextField(max_length=2000)
    news_section = models.ForeignKey(NewsSection, on_delete=models.CASCADE,blank=True)





class Partherns(models.Model):
    header = models.CharField(max_length=200, unique=False)
    text_description = models.TextField(max_length=2000)

    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name_plural = "12. Our Best Partherns"
    

class ParthernsImage(models.Model):
    icon = models.ImageField(verbose_name=_("image"), upload_to="media/parthers")
    parthers = models.ForeignKey(Partherns, on_delete=models.CASCADE,blank=True)
    



class Footer(models.Model):
    address_header = models.CharField(max_length=400)  
    address = models.TextField(max_length=400) 
    email_header = models.CharField(max_length=400) 
    email1 = models.EmailField(_("email"), max_length=254)
    email2 = models.EmailField(_("email2"), max_length=254,blank=True,null=True)
    phone_header = models.CharField(max_length=400) 
    phone =  models.CharField(max_length=200, unique=False)
    phone2 =  models.CharField(max_length=200, unique=False,blank=True,null=True)
    text_under_line = models.CharField(_("text copy right"), max_length=200)

    class Meta:
        verbose_name_plural = "13. Footer"

class Logo(models.Model):
    logo = models.ImageField(_("logo"), upload_to="media/image/logo",help_text = "logo must be width 113 px and height 41 px.")

    def __str__(self):
        return self.logo.url
    