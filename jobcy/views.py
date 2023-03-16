from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from AboutUs.models import AboutUs
from ContactUs.models import FollowUs, Location
from content .models import (
    Footer,
    Logo,
    NewsSection,
    NumbersSection,
    Partherns,
    PorfolioItem,
    Portfolio,
    Progress,
    SectionFiveOurTeams,
    SectionFourProfessional,
    SectionSixCustomersSay,
    SectionThree,
    SectionThreeIcon,
    SectionTwo, 
    SectionUnderSliderIcon, 
    Slider, 
    SectionUnderSlider
)


def homePage(request):
    slider = Slider.objects.all()
    sectionUnderSlider = SectionUnderSlider.objects.all().first()
    sectionUnderSliderIcon = SectionUnderSliderIcon.objects.all()
    sectionTwo = SectionTwo.objects.all().first()
    progress = Progress.objects.all()
    numbers = NumbersSection.objects.all()
    sectionThree = SectionThree.objects.all().first()
    sectionThreeIcons = SectionThreeIcon.objects.all()
    portfolio = Portfolio.objects.all().first()
    porfolioItem = PorfolioItem.objects.all()
    sectionFourProfessional = SectionFourProfessional.objects.all().first()
    sectionFiveOurTeam = SectionFiveOurTeams.objects.all().first()
    sectionSixCustomersSay = SectionSixCustomersSay.objects.all().first() 
    newsSection = NewsSection.objects.all().first() 
    partherns = Partherns.objects.all().first() 
    footer = Footer.objects.all().first() 
    logo = Logo.objects.all().first() 
    follow_us = FollowUs.objects.all().first()
    context={
        'sliders': slider,
        'sectionUnderSliders': sectionUnderSlider,
        'sectionUnderSliderIcons' : sectionUnderSliderIcon,
        'sectionTwo' : sectionTwo,
        'progress' : progress,
        'numbers' : numbers,
        'sectionThrees': sectionThree,
        'sectionThreeIcons' : sectionThreeIcons,
        'portfolio' : portfolio,
        'porfolioItems' : porfolioItem,
        'sectionFourProfessional' : sectionFourProfessional,
        'sectionFiveOurTeam' : sectionFiveOurTeam,
        'sectionSixCustomersSay' : sectionSixCustomersSay,
        'newsSection' : newsSection,
        'partherns' : partherns,
        'footer' : footer,
        'logo' : logo,
        'follow_us' : follow_us,    
    }
    return render(request,'base.html',context)



from AboutUs.models import SectionTwo as Sectiontwo
def aboutUs(request):
    footer = Footer.objects.all().first() 
    about_us = AboutUs.objects.all()
    numbers = NumbersSection.objects.all()
    section_two = Sectiontwo.objects.all().first()
    partherns = Partherns.objects.all().first() 
    logo = Logo.objects.all().first() 
    context={
        'footer' : footer,
        'about_us' : about_us,
        'numbers' : numbers,        
        'section_two' : section_two,     
        'partherns' : partherns,
        'logo' : logo,
    }
    return render(request,'about_us.html',context)



from ContactUs.forms import ContactUsForm
def contactUs(request):
    form = ContactUsForm
    if request.method == "POST":
        form = ContactUsForm(request.POST,request.FILES)
        print("_______________________________________________________________________")
        if form.is_valid():
            contact_us = form
            contact_us.save()
            form=ContactUsForm()
    footer = Footer.objects.all().first()
    follow_us = FollowUs.objects.all().first()
    location = Location.objects.all().first()
    logo = Logo.objects.all().first() 
    context={
        'footer' : footer,
        'follow_us' : follow_us,
        'form': form,
        'location' : location,
        'logo' : logo,
    }
    return render(request,'contact_us_3.html', context)



def error_404_view(request, exception):
    logo = Logo.objects.all().first()
    footer = Footer.objects.all().first() 
    context={
        'footer' : footer,
        'logo' : logo,
    }
    return render(request, '404.html', context)
# hello github