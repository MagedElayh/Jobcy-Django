from django.urls import path
# urls.py
from contact import views

urlpatterns = [
    # Contact
    path('contact',views.ContactView.as_view(),name='contact'),
]