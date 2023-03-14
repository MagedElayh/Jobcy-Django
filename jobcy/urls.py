from django.contrib import admin
from django.urls import path,include

from jobcy import settings
# urls.py
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Index Page
    path('', views.homePage,name='index'),
    path('index', views.homePage,name='index-2'),

    path('aboutus/',views.aboutUs, name='about-us'),
    path('contact/',views.contactUs,name='contact-us'),

    path('', include('pages.urls')),
    
    # add a flag for
    # handling the 404 error
    
    # path('index-2/', views.Index2.as_view(),name='index-2'),
    # path('index-3/', views.Index3.as_view(),name='index-3'),

    # # Company
    # path('company/',include('company.urls')),

    # # Pages
    # path('pages/',include('pages.urls')),

    # # Blog
    # path('blog/',include('blog.urls')),

    # # Contact
    # path('',include('contact.urls')),
    
    # # Manage-Jobs
    # path('manage-jobs',views.ManageJobs.as_view(),name='manage-jobs'),
    # path('manage-jobs-post',views.ManageJobs.as_view(),name='manage-jobs-post'),
    # path('bookmark-jobs',views.BookmarkJobs.as_view(),name='bookmark-jobs'),
    # path('profile',views.Profile.as_view(),name='profile'),
]

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.error_404_view