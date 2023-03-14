# from numbers import Number
from django.contrib import admin

from .models import *
# Register your models here.
# admin.site.register(Header)
admin.site.register(Slider)

admin.site.register(NumbersSection)

admin.site.register(Portfolio)
# admin.site.register(PorfolioItem)



# admin.site.register(SectionUnderSlider)
# admin.site.register(SectionUnderSliderIcon)

# admin.site.register(SectionTwo)
# admin.site.register(Progress)






class ProgressIconInline(admin.TabularInline):
    model = Progress
    readonly_fields = ('id',)
    extra = 1

@admin.register(SectionTwo)
class SectionTwoAdmin(admin.ModelAdmin):
    inlines = [ProgressIconInline,]





class SectionUnderSliderIconInline(admin.TabularInline):
    model = SectionUnderSliderIcon
    readonly_fields = ('id',)
    extra = 1

@admin.register(SectionUnderSlider)
class SectionUnderSliderAdmin(admin.ModelAdmin):
    inlines = [SectionUnderSliderIconInline,]





class porfolioDetailInline(admin.TabularInline):
    model = porfolioDetail
    readonly_fields = ('id',)
    extra = 1

@admin.register(PorfolioItem)
class PorfolioItemAdmin(admin.ModelAdmin):
    inlines = [porfolioDetailInline,]




class SectionSixCustomersSayline(admin.TabularInline):
    model = CustomersSay
    readonly_fields = ('id',)
    extra = 1

@admin.register(SectionSixCustomersSay)
class PorfolioItemAdmin(admin.ModelAdmin):
    inlines = [SectionSixCustomersSayline,]

# admin.site.register(SectionThree)
# admin.site.register(SectionThreeIcon)

class SectionThreeIconline(admin.TabularInline):
    model = SectionThreeIcon
    readonly_fields = ('id',)
    extra = 1

@admin.register(SectionThree)
class SectionThreeAdmin(admin.ModelAdmin):
    inlines = [SectionThreeIconline,]






class NewsImageline(admin.TabularInline):
    model = NewsImage
    readonly_fields = ('id',)
    extra = 1

@admin.register(NewsSection)
class PorfolioItemAdmin(admin.ModelAdmin):
    inlines = [NewsImageline,]





class SectionImageInline(admin.TabularInline):
    model = SectionImage
    readonly_fields = ('id',)
    extra = 1

@admin.register(SectionFiveOurTeams)
class SectionFiveOurTeamsAdmin(admin.ModelAdmin):
    inlines = [SectionImageInline,]





class ParthernsImageline(admin.TabularInline):
    model = ParthernsImage
    readonly_fields = ('id',)
    extra = 1

@admin.register(Partherns)
class ParthernsAdmin(admin.ModelAdmin):
    inlines = [ParthernsImageline,]




# admin.site.register(porfolioDetail)
admin.site.register(SectionFourProfessional)
admin.site.register(Footer)
admin.site.register(Logo)

