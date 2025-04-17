from django.urls import path
from .views import palindrome_check, temp_conversion

from pages import views
from pages.views import HomePageView, AboutPageView, ContactPageView, SoftwareTestingPageView, FindGeoLocPageView, \
    CheckPalindromePageView, TempConversionPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('software-testing/', SoftwareTestingPageView.as_view(), name='software-testing'),
    path('find-geo-loc/', FindGeoLocPageView.as_view(), name='find-geo-loc'),
    path('check-palindrome/', CheckPalindromePageView.as_view(), name='check-palindrome'),
    path('temperature-conversion/', TempConversionPageView.as_view(), name='temperature-conversion'),
    path('palindrome-check/', palindrome_check, name='palindrome_check'),
    path('temp-conversion/', temp_conversion, name='temp_conversion'),
]